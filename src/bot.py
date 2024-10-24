import os
from typing import Dict, List
from .utils import detect_crisis_keywords, sanitize_input, format_chat_history
from .prompts import CRISIS_KEYWORDS, CRISIS_RESPONSE, LOCATION_PROMPT, GENERAL_RESOURCES
from .chain import create_therapy_chain
from .events import EventTracker
from config import EVENTS_DIR, EVENT_TRACKING
from .resources import find_resources, get_location_based_resources  # Updated import

class TherapyBot:
    def __init__(self, api_key: str, model_name: str, temperature: float):
        self.chain = create_therapy_chain(api_key, model_name, temperature)
        self.event_tracker = EventTracker(EVENTS_DIR) if EVENT_TRACKING else None
        self.awaiting_location = False  # Flag to track if bot is awaiting location input

    def _track_interaction(self, user_input: str, bot_response: str, is_crisis: bool = False):
        """Track interaction details."""
        if self.event_tracker:
            event_data = {
                "user_input": user_input,
                "bot_response": bot_response,
                "is_crisis": is_crisis,
                
            }
            self.event_tracker.track_event("interaction", event_data)
            
            if is_crisis:
                self.event_tracker.track_event("crisis_detected", {
                    "user_input": user_input,
                })

    def generate_response(self, user_input: str, chat_history: List[Dict] = None) -> str:
        """Generate response using the LangChain conversation chain."""
        clean_input = sanitize_input(user_input)

        # Check for crisis keywords
        is_crisis = detect_crisis_keywords(clean_input, CRISIS_KEYWORDS)
        if is_crisis:
            self._track_interaction(clean_input, CRISIS_RESPONSE, is_crisis=True)
            return CRISIS_RESPONSE

        # Handle location input for resource recommendation
        if self.awaiting_location:
            location_based_resources = get_location_based_resources(clean_input)
            self.awaiting_location = False  # Reset the flag
            self._track_interaction(clean_input, location_based_resources)
            return location_based_resources

        # Check for resource-related keywords
        if any(keyword in clean_input for keyword in ["resources", "help", "support"]):
            # Ask user for their location
            self.awaiting_location = True
            self._track_interaction(clean_input, LOCATION_PROMPT)
            return LOCATION_PROMPT

        try:
            # Format chat history if provided
            if chat_history:
                formatted_history = format_chat_history(chat_history)
                self.chain.memory.chat_memory.messages = formatted_history

            response = self.chain.predict(input=clean_input)
            
            self._track_interaction(clean_input, response)
            return response

        except Exception as e:
            error_msg = "I apologize, but I'm having trouble responding right now. Please try again or reach out to a mental health professional if you need immediate assistance."
            print(f"⚠️ Error generating response: {str(e)}")
            self._track_interaction(clean_input, error_msg, is_crisis=False)
            return error_msg
