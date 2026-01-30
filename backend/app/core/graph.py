from langgraph.types import Send
from langchain_openai.chat_models import ChatOpenAI
from langchain.agents import create_agent
from langchain_core.messages import SystemMessage, AIMessage, HumanMessage,ToolMessage
from langchain_tavily import TavilySearch
from langgraph.graph import START, StateGraph, END

from app.schemas.state import (
    OverAllState,
    ReflectionState,
    QueryGenerationState
)
from app.schemas.schemas import SearchQueryList,Reflection
from app.core.prompts import (
    query_writer_instructions,
    get_current_date, 
    web_searcher_instructions,
    reflection_instructions,
    answer_instructions
)
from app.core.config import settings
from app.utils.utils import get_research_topic

from typing import List
from rich.console import Console
import json
import logging
import os

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Use settings from pydantic-settings (already validated)
TAVILY_API_KEY = settings.TAVILY_API_KEY
API_KEY = settings.API_KEY
BASE_URL = settings.BASE_URL


os.environ['TAVILY_API_KEY'] = TAVILY_API_KEY





def generate_query(state: OverAllState) -> QueryGenerationState:
    """
    Generate search queries for a given research topic.

    Args:
        research_topic: The topic to research
        number_queries: Number of queries to generate

    Returns:
        QueryGenerationState with generated search queries
    """
    try:
        llm = ChatOpenAI(
            model="minimax/minimax-m2.1",
            api_key=API_KEY,
            base_url=BASE_URL,
            temperature=1.0,
            max_retries=2
        )

        research_topic = get_research_topic(state['messages'])

        number_queries = state.get("initial_search_query_count", settings.number_of_initial_queries)
        print(f"最多生成:{number_queries}个查询")
        system_prompt = query_writer_instructions.format(
            current_date=get_current_date(),
            research_topic=research_topic,
            number_queries=number_queries,
        )

        agent = create_agent(
            model=llm,
            response_format=SearchQueryList
        )

        result = agent.invoke(
            {
                "messages": [SystemMessage(system_prompt)]
            }
        )
        response = result.get('structured_response', '')

        print(response.query, '---------------------------')
        return {
            "search_query": response.query
        }

    except Exception as e:
        logger.error(f"Error generating search queries: {e}")
        raise


def continue_to_web_search(state: OverAllState):
    """
     用于生成n个网络研究节点，每个搜索查询对应一个节点
     这实现了并行搜索处理
    """
    return [
         Send("web_search", {
            "search_query": query,
            "id": int(idx)
         }) for idx, query in enumerate(state["search_query"])
     ]

def web_search(state: OverAllState) -> OverAllState:
    """
    Perform web search using the given queries.

    Args:
        query: List of search queries to execute

    Returns:
        Search results from the web
    """
    try:
        llm = ChatOpenAI(
            model="minimax/minimax-m2.1",
            api_key=API_KEY,
            base_url=BASE_URL,
            temperature=0
        )

        search_prompt = web_searcher_instructions.format(
            current_date=get_current_date(),
            research_topic=state['search_query']
        )
        tavily_search_tool = TavilySearch(
            max_results=5,
            topic="general"
        )

        agent = create_agent(
            model=llm,
            system_prompt=search_prompt,
            tools=[tavily_search_tool],
        )

        response = agent.invoke({
            "input": ""
        })

        messages = response.get('messages', [])

        return_state: OverAllState = {
            "search_query": [state['search_query']],  # 必须是列表，因为使用了 operator.add
        }
    
        for msg in messages:
            Console().print(f"消息类型: {type(msg)}, 是否为ToolMessage: {isinstance(msg, ToolMessage)}")
            if isinstance(msg, ToolMessage) and msg and msg.content:            
                try:
                  data = json.loads(msg.content)
                  results = data.get("results", [])
                  print(f"JSON解析成功: {type(data)}")
                  return_state["web_search_results"] = results
                except json.JSONDecodeError as je:
                  print(f"JSON解析也失败: {je}")    
        return return_state
    except Exception as e:
        logger.error(f"Error performing web search: {e}")
        raise


def reflection_answer(state: OverAllState) -> ReflectionState:
    
      state['research_loop_count'] = state.get('research_loop_count', 0) + 1
      current_date = get_current_date()
      current_topic = get_research_topic(state['messages'])

      pre_search_results = state.get("web_search_results")

      json_str_result = [
         json.dumps(item, ensure_ascii=False) for item in pre_search_results
      ]

      reflection_prompt = reflection_instructions.format(
         current_date=current_date,
         research_topic=current_topic,
         summaries="\n\n---\n\n".join(json_str_result)
      )

      llm = ChatOpenAI(
            model="minimax/minimax-m2.1",
            api_key=API_KEY,
            base_url=BASE_URL,
            temperature=1.0,
            max_retries=2
       )

      agent = create_agent(
         model=llm,
         system_prompt=reflection_prompt,
         response_format=Reflection
       )
      response = agent.invoke({
         "input": ""
       })

      reflection_result = response.get('structured_response', '')

      return {
         "is_sufficient": reflection_result.is_sufficient,
         "knowledge_gap": reflection_result.knowledge_gap,
         "follow_up_queries": reflection_result.follow_up_queries,
         "research_loop_count": state['research_loop_count'],
         "number_of_ran_queries": len(state["search_query"])
      }

def evaluate_research(state: ReflectionState) -> OverAllState:
     
     # 收集信息还是基于配置的最大研究循环数完成摘要来控制研究循环
     max_research_loops = (
        state.get('max_research_count') 
        if state.get('max_research_count') is not None
        else settings.max_research_loops
     )

     if state['is_sufficient'] or state['research_loop_count'] >= max_research_loops:
         # 返回最终回答
         return 'final_answer'
     else:
       return [
        Send("web_search", {
            "search_query": follup_query,
            "id": state["number_of_ran_queries"] + int(idx)
        }) for idx, follup_query in enumerate(state["follow_up_queries"])
        ]

def final_answer(state: OverAllState):

      pre_search_results = state.get("web_search_results")

      json_str_result = [
         json.dumps(item, ensure_ascii=False) for item in pre_search_results
      ]
      
      final_answer_prompt = answer_instructions.format(
        current_date=get_current_date(),
        research_topic=get_research_topic(state['messages']),
        summaries="\n\n---\n\n".join(json_str_result)
      )

      llm = ChatOpenAI(
            model="minimax/minimax-m2.1",
            api_key=API_KEY,
            base_url=BASE_URL,
            temperature=0,
            max_retries=2
       )
       
      agent = create_agent(model=llm, system_prompt=final_answer_prompt)

      response = agent.invoke({"input": ""})

      respponse_messages = response.get('messages', [])
      content = respponse_messages[-1].content


      return {
        "messages": [AIMessage(content=content)]
      }




def create_agent_graph():

     graph = StateGraph(OverAllState)
     graph.add_node('generate_query', generate_query)
     graph.add_node('web_search', web_search)
     graph.add_node('reflection', reflection_answer)
     graph.add_node("final_answer", final_answer)
     graph.add_edge(START, 'generate_query')
     graph.add_conditional_edges("generate_query", continue_to_web_search, ["web_search"])
     graph.add_edge('web_search', 'reflection')
     graph.add_conditional_edges("reflection", evaluate_research, ["web_search", "final_answer"])
     graph.add_edge('final_answer', END)

     return graph.compile(name="reflection_agent")    


export_graph = create_agent_graph()
# # Remove test code from production
# if __name__ == "__main__":
#     agent_graph = create_agent_graph()
#     response = agent_graph.invoke({
#         "messages": [HumanMessage("What is the capital of France?")]
#     })
  
#     for msg in response.get('messages', []):
#         Console().print(msg.content)
