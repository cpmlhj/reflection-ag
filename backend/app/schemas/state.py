from typing import TypedDict, Annotated, List
from langgraph.graph import add_messages
from langchain.messages import AnyMessage

import operator

class Query(TypedDict):
    query: str
    rationale: str

class QueryResult(TypedDict):
    url: str
    title: str
    content: str
    score: int
    raw_content: str | None

# Agent state
class OverAllState(TypedDict):
    messages: Annotated[AnyMessage, add_messages]
    search_query: Annotated[List[str], operator.add]
    web_search_results: Annotated[List[QueryResult], operator.add]
    max_research_count: int
    research_loop_count: int


# Query generation state
class QueryGenerationState(TypedDict):
    search_query: List[QueryResult]

# Reflection state
class ReflectionState(TypedDict):
    is_sufficient: bool
    knowledge_gap: str
    follow_up_queries: Annotated[List[str], operator.add]
    research_loop_count: int