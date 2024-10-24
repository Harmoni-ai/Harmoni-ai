# Mental Health Chatbot

This project is a **Mental Health Support Chatbot** designed to engage users in empathetic conversations and provide emotional support. The chatbot uses a language model to generate responses and recognize crisis situations. It is **not** a replacement for professional mental health care but can help users explore their emotions, validate their feelings, and suggest helpful resources.

## Features

### 1. Empathetic Conversational Style
The chatbot is designed to interact with users in an empathetic manner, ensuring that it:
- Provides non-judgmental responses
- Shows care and understanding
- Validates the user's feelings
- Encourages users to express their emotions
- Suggests healthy coping strategies

### 2. Crisis Detection
The chatbot can detect keywords related to crisis situations (e.g., "suicide", "want to die") and respond with appropriate emergency resources, including the **National Crisis Hotline (988)** and **Emergency Services (911)**.

### 3. Memory and Context Awareness
The chatbot uses memory to maintain context across the conversation, allowing it to provide more meaningful responses based on previous user inputs.

### 4. Event Tracking
The chatbot tracks user interactions and saves them for potential analysis, such as monitoring crisis detection or user behavior over time.

## Tech Stack

- **Frontend**: [Streamlit](https://streamlit.io/) (for the user interface)
- **Backend**: Python (with LangChain for conversation management)
- **LLM**: Groq-based LLM (e.g., `llama3-8b-8192`) for generating responses
- **Database**: Pinecone vector database (for efficient storage of chat history and embeddings)
- **Environment Configuration**: `dotenv` for managing environment variables

## File Structure

```
mental-health-chatbot/
│
├── README.md                # Project documentation
├── main.py                  # Streamlit app for UI and chatbot interaction
├── config.py                # Configuration file for API keys, model names, etc.
├── bot.py                   # Core chatbot logic, response generation, crisis detection
├── chain.py                 # Therapy chain creation using LangChain
├── events.py                # Event tracking functionality
├── prompts.py               # Custom prompts for empathetic conversations and crisis handling
├── utils.py                 # Utility functions for sanitizing inputs, formatting chat history
├── .env                     # Environment variables (API keys, etc.)
├── requirements.txt         # List of required Python packages
└── src/
    └── __init__.py          # Init file for the source folder

```

# Installation and Setup

## Prerequisites

- **Python 3.8+** installed
- **Pinecone** and **Groq API keys** for database and LLM access
- **Streamlit** for building the web-based interface

## Steps for Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/mental-health-chatbot.git
   cd mental-health-chatbot
   ```

2. **Install packages**:
    ```bash
    pip install -r requirements.txt
    ```
3. **Setup config.py**:
    ```bash
    GROQ_API_KEY = os.getenv("Your_API_Key")
    MODEL_NAME = "llama3-8b-8192"
    TEMPERATURE = 0.7
    ```
4. **Run The Application**:
   ```bash
   streamlit run main.py
   ```


### Build with ❤️ by team harmoni.ai

