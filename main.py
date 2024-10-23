import streamlit as st
from src.bot import TherapyBot
from config import GROQ_API_KEY, MODEL_NAME, TEMPERATURE

def main():
    st.title("Mental Health Support Chat")
    st.write("I'm here to listen and support you. Remember, I'm an AI assistant and not a replacement for professional mental health care.")

    # Initialize bot
    if 'bot' not in st.session_state:
        st.session_state.bot = TherapyBot(
            api_key='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',
            model_name=MODEL_NAME,
            temperature=0.7
        )

    # Initialize chat history
    if 'messages' not in st.session_state:
        st.session_state.messages = []

    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Chat input
    if prompt := st.chat_input("How are you feeling today?"):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Generate and display assistant response
        with st.chat_message("assistant"):
            response = st.session_state.bot.generate_response(
                prompt, 
                chat_history=st.session_state.messages[:-1]  # Exclude current message
            )
            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    main()