from langchain_groq import ChatGroq
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.callbacks import StreamingStdOutCallbackHandler
from .prompts import CHAT_PROMPT

def create_therapy_chain(api_key: str, model_name: str, temperature: float):
    """Create a LangChain conversation chain for the therapy bot."""
    
    # Initialize the Groq LLM
    llm = ChatGroq(
        groq_api_key='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',
        model_name='llama3-8b-8192',
        temperature=0.7,
        streaming=True,
        callbacks=[StreamingStdOutCallbackHandler()]
    )
    
    # Initialize memory
    memory = ConversationBufferMemory(
        return_messages=True,
        memory_key="chat_history"
    )
    
    # Create the conversation chain
    chain = ConversationChain(
        llm=llm,
        memory=memory,
        prompt=CHAT_PROMPT,
        verbose=True
    )
    
    return chain

