# from typing import List, Dict, Union
# import re
# from langchain_core.messages import HumanMessage, AIMessage



# def sanitize_input(text: str) -> str:
#     """Clean and sanitize user input."""
#     text = re.sub(r'[^\w\s.,!?-]', '', text)
#     return text.strip()

# def format_chat_history(messages: List[Dict]) -> List[Union[HumanMessage, AIMessage]]:
#     """Convert chat history to LangChain message format."""
#     formatted_messages = []
#     for msg in messages:
#         if msg["role"] == "user":
#             formatted_messages.append(HumanMessage(content=msg["content"]))
#         elif msg["role"] == "assistant":
#             formatted_messages.append(AIMessage(content=msg["content"]))
#     return formatted_messages


import re
from typing import List, Dict, Union
from langchain_core.messages import HumanMessage, AIMessage

def sanitize_input(text: str) -> str:
    """Clean and sanitize user input."""
    text = re.sub(r'[^\w\s.,!?-]', '', text)  # Sanitize for text-based input
    return text.strip()

def detect_crisis_keywords(text: str, keywords: List[str]) -> bool:
    """Check if any crisis keywords are present in the text."""
    text = text.lower()
    return any(keyword in text for keyword in keywords)

def format_chat_history(messages: List[Dict]) -> List[Union[HumanMessage, AIMessage]]:
    """Convert chat history to LangChain message format."""
    formatted_messages = []
    for msg in messages:
        if msg["role"] == "user":
            formatted_messages.append(HumanMessage(content=msg["content"]))
        elif msg["role"] == "assistant":
            formatted_messages.append(AIMessage(content=msg["content"]))
    return formatted_messages
