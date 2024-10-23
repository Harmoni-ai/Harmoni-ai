from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder, SystemMessagePromptTemplate, HumanMessagePromptTemplate

SYSTEM_TEMPLATE = """You are a supportive mental health chatbot assistant. Your role is to:
1. Provide empathetic, non-judgmental responses
2. Help users explore their thoughts and feelings
3. Suggest healthy coping strategies
4. Recognize crisis situations and direct to professional help
5. Maintain clear boundaries and remind users you're an AI assistant

Important: Always refer users to professional mental health services for serious concerns.
Emergency contacts to provide when needed:
- National Crisis Line: 988
- Emergency Services: 911"""

CHAT_PROMPT = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(SYSTEM_TEMPLATE),
    MessagesPlaceholder(variable_name="chat_history"),
    HumanMessagePromptTemplate.from_template("{input}")
])

CRISIS_KEYWORDS = [
    "suicide", "kill myself", "want to die", "end it all",
    "self-harm", "hurt myself", "cutting"
]

CRISIS_RESPONSE = """I hear that you're going through a really difficult time. Your life has value and there are people who want to help:

1. Please call 988 (National Crisis Hotline) - they're available 24/7
2. Go to the nearest emergency room
3. Call 911 if you're in immediate danger
4. Contact a mental health professional

Would you like help finding mental health resources in your area?"""
