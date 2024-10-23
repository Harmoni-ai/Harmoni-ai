from typing import Dict, List
from datetime import datetime
from .utils import detect_crisis_keywords, sanitize_input, format_chat_history
from .prompts import CRISIS_KEYWORDS, CRISIS_RESPONSE
from .chain import create_therapy_chain
from .events import EventTracker
from config import EVENTS_DIR, EVENT_TRACKING

class TherapyBot:
    def __init__(self, api_key: str, model_name: str, temperature: float):
        self.chain = create_therapy_chain(api_key, model_name, temperature)
        self.event_tracker = EventTracker(EVENTS_DIR) if EVENT_TRACKING else None

    def _track_interaction(self, user_input: str, bot_response: str, is_crisis: bool = False):
        """Track interaction details."""
        if self.event_tracker:
            event_data = {
                "user_input": user_input,
                "bot_response": bot_response,
                "is_crisis": is_crisis,
                "timestamp": datetime.now().isoformat()
            }
            self.event_tracker.track_event("interaction", event_data)
            
            if is_crisis:
                self.event_tracker.track_event("crisis_detected", {
                    "user_input": user_input,
                    "timestamp": datetime.now().isoformat()
                })

    def generate_response(self, user_input: str, chat_history: List[Dict] = None) -> str:
        """Generate response using the LangChain conversation chain."""
        # Sanitize input
        clean_input = sanitize_input(user_input)
        
        # Check for crisis keywords
        is_crisis = detect_crisis_keywords(clean_input, CRISIS_KEYWORDS)
        if is_crisis:
            self._track_interaction(clean_input, CRISIS_RESPONSE, is_crisis=True)
            return CRISIS_RESPONSE

        try:
            # Format chat history if provided
            if chat_history:
                formatted_history = format_chat_history(chat_history)
                self.chain.memory.chat_memory.messages = formatted_history

            # Generate response
            response = self.chain.predict(input=clean_input)
            
            # Track interaction
            self._track_interaction(clean_input, response)
            
            return response

        except Exception as e:
            error_msg = "I apologize, but I'm having trouble responding right now. Please try again or reach out to a mental health professional if you need immediate assistance."
            print(f"⚠️ Error generating response: {str(e)}")
            self._track_interaction(clean_input, error_msg, is_crisis=False)
            return error_msg
