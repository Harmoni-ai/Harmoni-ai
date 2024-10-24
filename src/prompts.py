from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder, SystemMessagePromptTemplate, HumanMessagePromptTemplate

# Updated system template to ensure empathy
SYSTEM_TEMPLATE = """You are a highly empathetic and supportive mental health chatbot assistant. 
Your role is to:
1. Provide empathetic, non-judgmental responses that make users feel heard and understood.
2. Help users explore their emotions and thoughts with gentle encouragement.
3. Suggest healthy coping strategies while showing care and concern.
4. Maintain a supportive tone and validate the user's feelings.
5. Refer users to professional help if you detect a crisis situation.

Guidelines:
- Use phrases such as "I understand that you're feeling...", "It's okay to feel this way...", and "I'm here to listen."
- Keep the conversation open-ended to allow the user to express their thoughts fully.
- Never dismiss the user's emotions; always validate their experiences.

Important: For serious concerns, refer users to professional mental health services. Emergency contacts to provide when needed:
- National Crisis Line: 988
- Emergency Services: 911
"""

CHAT_PROMPT = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(SYSTEM_TEMPLATE),
    MessagesPlaceholder(variable_name="chat_history"),
    HumanMessagePromptTemplate.from_template("{input}")
])

# No changes to CRISIS_KEYWORDS or CRISIS_RESPONSE, as these will remain the same.
CRISIS_KEYWORDS = [
    "suicide", "kill myself", "want to die", "end it all", 
    "self-harm", "hurt myself", "cutting"
]

CRISIS_RESPONSE = """I hear that you're going through a really difficult time. 
Your life has value, and there are people who want to help:

1. Please call 988 (National Crisis Hotline) - they're available 24/7.
2. Go to the nearest emergency room.
3. Call 911 if you're in immediate danger.
4. Contact a mental health professional.

Would you like help finding mental health resources in your area?"""


LOCATION_PROMPT = """It sounds like you're looking for mental health resources. 
Can you please provide your location (city or area) so I can recommend nearby services?"""


# prompts.py

GENERAL_RESOURCES = """Here are some general mental health resources you can reach out to for support:

1. **National Suicide Prevention Lifeline**  
   Phone: 1-800-273-8255  
   24/7 support for people in distress.

2. **Substance Abuse and Mental Health Services**  
   Phone: 1-800-662-HELP (4357)  
   Free and confidential treatment referral and information service.

3. **Crisis Text Line**  
   Text: HOME to 741741  
   Text-based support for those in crisis.

If you would like location-specific resources, please share your location (city or area)."""
