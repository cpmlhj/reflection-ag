from unittest import result
from langgraph.types import Send
from langchain_openai.chat_models import ChatOpenAI
from langchain.agents import create_agent
from langchain_core.messages import SystemMessage, AIMessage, HumanMessage,ToolMessage
from langchain_tavily import TavilySearch


from app.schemas.state import (
    OverAllState,
    ReflectionState,
    QueryGenerationState
)
from app.schemas.schemas import SearchQueryList
from app.core.prompts import query_writer_instructions, get_current_date, web_searcher_instructions

from typing import List
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load API keys from environment variables
TAVILY_API_KEY = os.environ.get("TAVILY_API_KEY")
API_KEY = os.environ.get("API_KEY")
BASE_URL = os.environ.get("BASE_URL", "https://openrouter.ai/api/v1")

# Validate required environment variables
if not TAVILY_API_KEY:
    raise ValueError("TAVILY_API_KEY environment variable is not set")
if not API_KEY:
    raise ValueError("API_KEY environment variable is not set")

os.environ["TAVILY_API_KEY"] = TAVILY_API_KEY





def generate_query(research_topic: str = "Who won the 2018 NBA championship", number_queries: int = 3) -> QueryGenerationState:
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
        return {
            "search_query": response.query
        }

    except Exception as e:
        logger.error(f"Error generating search queries: {e}")
        raise


def web_search(query: List[str]):
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
            research_topic=query
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

        for msg in messages:
            if isinstance(msg, ToolMessage):
                logger.info(f"Search result: {msg.content}")

        return messages

    except Exception as e:
        logger.error(f"Error performing web search: {e}")
        raise


# Remove test code from production
# if __name__ == "__main__":
#     query = generate_query()
#     web_search(query)
