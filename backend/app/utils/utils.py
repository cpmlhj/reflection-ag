

from typing import List

from langchain.messages import AIMessage, AnyMessage, HumanMessage


def get_research_topic(messages: List[AnyMessage]) -> str:
    """
    从消息列表中提取研究主题
    
    Args:
        messages: 包含用户和AI消息的列表
        
    Returns:
        str: 提取的研究主题字符串
    """
    # 检查请求是否有历史记录，并将消息合并为单个字符串
    if len(messages) == 1:
        return messages[-1].content

    else:
        research_topic = ""
        for msg in messages:
            if isinstance(msg, HumanMessage):
                research_topic += f"User: {msg.content} \n"  
            elif isinstance(msg, AIMessage):
                research_topic += f"Assistant: {msg.content}\n"   

        return research_topic          