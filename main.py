import streamlit as st
import pyttsx3
from src.bot import TherapyBot
from config import GROQ_API_KEY, MODEL_NAME, TEMPERATURE

def main():
    st.title("Empathetic Mental Health Support Chat")
    st.write("I'm here to listen and support you with empathy. Remember, I'm an AI assistant and not a replacement for professional mental health care.")

    # Initialize the bot
    if 'bot' not in st.session_state:
        st.session_state.bot = TherapyBot(
            api_key=GROQ_API_KEY,
            model_name=MODEL_NAME,
            temperature=TEMPERATURE
        )

    # Initialize chat history
    if 'messages' not in st.session_state:
        st.session_state.messages = []

    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # User input with voice interaction
    col1, col2 = st.columns([3, 1])

    with col1:
        prompt = st.chat_input("How are you feeling today?")

    with col2:
        # Button to capture voice input
        if st.button("🎤 Speak"):
            # JS code to capture voice
            st.components.v1.html("""
                <script>
                    var recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
                    recognition.lang = 'en-US';
                    recognition.interimResults = false;
                    recognition.maxAlternatives = 1;

                    recognition.start();

                    recognition.onresult = function(event) {
                        const transcript = event.results[0][0].transcript;
                        const streamlitInput = document.getElementById("voice_input");
                        streamlitInput.value = transcript;
                        streamlitInput.dispatchEvent(new Event('change'));
                    };

                    recognition.onerror = function(event) {
                        console.error('Error occurred in recognition: ' + event.error);
                    };
                </script>
                <input type="text" id="voice_input" style="display:none;">
            """)

    # Process user input
    if prompt or st.session_state.get('voice_input'):
        user_input = prompt if prompt else st.session_state.get('voice_input', '')
        
        # Store the voice input in session state
        if user_input:
            st.session_state.messages.append({"role": "user", "content": user_input})
            with st.chat_message("user"):
                st.markdown(user_input)

            # Generate and display assistant response
            with st.chat_message("assistant"):
                response = st.session_state.bot.generate_response(
                    user_input,
                    chat_history=st.session_state.messages[:-1]  # Exclude current message
                )
                st.markdown(response)
                st.session_state.messages.append({"role": "assistant", "content": response})

            # Convert response to speech and play it
            play_voice(response)

def play_voice(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    main()
