from datetime import datetime
import json
import os
from typing import Dict, Any

class EventTracker:
    """Simple event tracking system for monitoring bot interactions."""
    
    def __init__(self, events_dir: str):
        self.events_dir = events_dir
        self.current_date = datetime.now().strftime("%Y-%m-%d")
        self.events_file = os.path.join(
            self.events_dir, 
            f"events_{self.current_date}.jsonl"
        )

    def track_event(self, event_type: str, data: Dict[str, Any]) -> None:
        """Track an event with timestamp and data."""
        if not os.path.exists(self.events_dir):
            os.makedirs(self.events_dir)
            
        event = {
            "timestamp": datetime.now().isoformat(),
            "type": event_type,
            "data": data
        }
        
        try:
            with open(self.events_file, "a") as f:
                f.write(json.dumps(event) + "\n")
        except Exception as e:
            print(f"⚠️ Error tracking event: {str(e)}")

    def get_recent_events(self, limit: int = 10) -> list:
        """Retrieve recent events."""
        events = []
        try:
            if os.path.exists(self.events_file):
                with open(self.events_file, "r") as f:
                    events = [json.loads(line) for line in f][-limit:]
        except Exception as e:
            print(f"⚠️ Error reading events: {str(e)}")
        return events
