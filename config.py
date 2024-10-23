from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()

GROQ_API_KEY = os.getenv("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")
MODEL_NAME = "llama3-8b-8192"  # Replace with actual model name
TEMPERATURE = 0.7

# Event tracking configuration
EVENT_TRACKING = True
EVENTS_DIR = "events"
if not os.path.exists(EVENTS_DIR):
    os.makedirs(EVENTS_DIR)