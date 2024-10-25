# import streamlit as st
# from src.bot import TherapyBot
# from config import GROQ_API_KEY, MODEL_NAME, TEMPERATURE
# from src.cbt_exercises import CBT_EXERCISES, get_personalized_exercises

# def chat_page():
#     st.title("Empathetic Mental Health Support Chat")
#     st.write("I'm here to listen and support you with empathy. Remember, I'm an AI assistant and not a replacement for professional mental health care.")

#     # Initialize the bot
#     if 'bot' not in st.session_state:
#         st.session_state.bot = TherapyBot(
#             api_key=GROQ_API_KEY,
#             model_name=MODEL_NAME,
#             temperature=TEMPERATURE
#         )

#     # Initialize chat history
#     if 'messages' not in st.session_state:
#         st.session_state.messages = []

#     # Display chat history
#     for message in st.session_state.messages:
#         with st.chat_message(message["role"]):
#             st.markdown(message["content"])

#     # User input
#     prompt = st.chat_input("How are you feeling today?")

#     if prompt:
#         st.session_state.messages.append({"role": "user", "content": prompt})
#         with st.chat_message("user"):
#             st.markdown(prompt)

#         # Generate and display assistant response
#         with st.chat_message("assistant"):
#             response = st.session_state.bot.generate_response(
#                 prompt,
#                 chat_history=st.session_state.messages[:-1]  # Exclude current message
#             )
#             st.markdown(response)
#             st.session_state.messages.append({"role": "assistant", "content": response})

# def cbt_exercise_page():
#     st.title("CBT Exercises")
    
#     # Mood Assessment
#     st.write("To get personalized CBT exercise recommendations, please select your current mood:")
#     mood = st.selectbox("Select your mood:", ["Neutral", "Anxious", "Depressed", "Stressed", "Happy"])
    
#     if st.button("Get Recommendations"):
#         recommended_exercises = get_personalized_exercises(mood)
#         st.write("We recommend the following exercises for you:")
#         for exercise in recommended_exercises:
#             st.write(f"- {exercise}")

#     # Exercise Selection
#     exercise = st.selectbox("Choose an exercise:", list(CBT_EXERCISES.keys()))

#     if st.button("Start Exercise"):
#         exercise_info = CBT_EXERCISES[exercise]
#         st.write(f"### {exercise}")
#         st.write(exercise_info["description"])
#         st.write("### Steps:")
#         for step in exercise_info["steps"]:
#             st.write(step)
        
#         # Journaling Input
#         st.write("### Reflection/Journaling")
#         journal_entry = st.text_area("Write your reflections after completing the exercise:")
        
#         if st.button("Save Journal Entry"):
#             # Here we would save the journal entry to a file or database
#             st.success("Your journal entry has been saved!")

# def main():
#     st.sidebar.title("Navigation")
#     page = st.sidebar.radio("Go to", ["Chat", "CBT Exercises"])

#     if page == "Chat":
#         chat_page()
#     elif page == "CBT Exercises":
#         cbt_exercise_page()

# if __name__ == "__main__":
#     main()





# import streamlit as st
# import speech_recognition as sr
# import pyttsx3
# from src.bot import TherapyBot
# from config import GROQ_API_KEY, MODEL_NAME, TEMPERATURE
# from src.cbt_exercises import CBT_EXERCISES, get_personalized_exercises

# # Initialize the text-to-speech engine globally
# tts_engine = pyttsx3.init()

# def speak_text(text):
#     """Convert text to speech and play it."""
#     # Ensure that the speaking happens in a separate thread
#     tts_engine.say(text)
#     tts_engine.runAndWait()

# def record_voice():
#     """Capture voice input and return the recognized text."""
#     recognizer = sr.Recognizer()
#     with sr.Microphone() as source:
#         st.info("Listening...")
#         audio = recognizer.listen(source)
#         try:
#             text = recognizer.recognize_google(audio)
#             return text
#         except sr.UnknownValueError:
#             st.error("Sorry, I could not understand the audio.")
#             return ""
#         except sr.RequestError:
#             st.error("Request error. Please check your internet connection.")
#             return ""

# def chat_page():
#     st.title("Empathetic Mental Health Support Chat")
#     st.write("I'm here to listen and support you with empathy. Remember, I'm an AI assistant and not a replacement for professional mental health care.")

#     # Initialize the bot
#     if 'bot' not in st.session_state:
#         st.session_state.bot = TherapyBot(
#             api_key=GROQ_API_KEY,
#             model_name=MODEL_NAME,
#             temperature=TEMPERATURE
#         )

#     # Initialize chat history
#     if 'messages' not in st.session_state:
#         st.session_state.messages = []

#     # Display chat history
#     for message in st.session_state.messages:
#         with st.chat_message(message["role"]):
#             st.markdown(message["content"])

#     # Voice or Text Input Option
#     input_method = st.radio("Choose your input method:", ["Text", "Voice"])
    
#     prompt = None  # Initialize prompt with None

#     if input_method == "Text":
#         prompt = st.chat_input("How are you feeling today?")
#     elif input_method == "Voice":
#         if st.button("Start Voice Input"):
#             prompt = record_voice()  # Capture voice input
#             if prompt:
#                 st.write(f"You said: {prompt}")

#     # Check if prompt contains valid input before processing
#     if prompt:
#         st.session_state.messages.append({"role": "user", "content": prompt})
#         with st.chat_message("user"):
#             st.markdown(prompt)

#         # Generate and display assistant response
#         with st.chat_message("assistant"):
#             response = st.session_state.bot.generate_response(
#                 prompt,
#                 chat_history=st.session_state.messages[:-1]  # Exclude current message
#             )
#             st.markdown(response)
#             st.session_state.messages.append({"role": "assistant", "content": response})
#             speak_text(response)  # Speak the response

# def cbt_exercise_page():
#     st.title("CBT Exercises")
    
#     # Mood Assessment
#     st.write("To get personalized CBT exercise recommendations, please select your current mood:")
#     mood = st.selectbox("Select your mood:", ["Neutral", "Anxious", "Depressed", "Stressed", "Happy"])
    
#     if st.button("Get Recommendations"):
#         recommended_exercises = get_personalized_exercises(mood)
#         st.write("We recommend the following exercises for you:")
#         for exercise, resource in recommended_exercises:
#             st.write(f"- {exercise} ([Resource]({resource}))")

#     # Exercise Selection
#     exercise = st.selectbox("Choose an exercise:", list(CBT_EXERCISES.keys()))

#     if st.button("Start Exercise"):
#         exercise_info = CBT_EXERCISES[exercise]
#         st.write(f"### {exercise}")
#         st.write(exercise_info["description"])
#         st.write("### Steps:")
#         for step in exercise_info["steps"]:
#             st.write(step)
        
#         # Journaling Input
#         st.write("### Reflection/Journaling")
#         journal_entry = st.text_area("Write your reflections after completing the exercise:")
        
#         if st.button("Save Journal Entry"):
#             # Here we would save the journal entry to a file or database
#             st.success("Your journal entry has been saved!")

# def main():
#     st.sidebar.title("Navigation")
#     page = st.sidebar.radio("Go to", ["Chat", "CBT Exercises"])

#     if page == "Chat":
#         chat_page()
#     elif page == "CBT Exercises":
#         cbt_exercise_page()

# if __name__ == "__main__":
#     main()

import streamlit as st
import speech_recognition as sr
from gtts import gTTS
import os
import tempfile
from playsound import playsound
from src.bot import TherapyBot
from config import GROQ_API_KEY, MODEL_NAME, TEMPERATURE
from src.cbt_exercises import CBT_EXERCISES, get_personalized_exercises

def speak_text(text):
    """Convert text to speech and play it."""
    # Create a temporary directory for the MP3 files
    with tempfile.TemporaryDirectory() as tmpdirname:
        mp3_file_path = os.path.join(tmpdirname, 'response.mp3')
        tts = gTTS(text=text, lang='en')
        tts.save(mp3_file_path)  # Save to the temporary file
        playsound(mp3_file_path)  # Play the audio file

def record_voice():
    """Capture voice input and return the recognized text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            st.error("Sorry, I could not understand the audio.")
            return ""
        except sr.RequestError:
            st.error("Request error. Please check your internet connection.")
            return ""

def chat_page():
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

    # Voice or Text Input Option
    input_method = st.radio("Choose your input method:", ["Text", "Voice"])
    
    prompt = None  # Initialize prompt with None

    if input_method == "Text":
        prompt = st.chat_input("How are you feeling today?")
    elif input_method == "Voice":
        if st.button("Start Voice Input"):
            prompt = record_voice()  # Capture voice input
            if prompt:
                st.write(f"You said: {prompt}")

    # Check if prompt contains valid input before processing
    if prompt:
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
            speak_text(response)  # Speak the response

def cbt_exercise_page():
    st.title("CBT Exercises")
    
    # Mood Assessment
    st.write("To get personalized CBT exercise recommendations, please select your current mood:")
    mood = st.selectbox("Select your mood:", ["Neutral", "Anxious", "Depressed", "Stressed", "Happy"])
    
    if st.button("Get Recommendations"):
        recommended_exercises = get_personalized_exercises(mood)
        st.write("We recommend the following exercises for you:")
        for exercise in recommended_exercises:
            st.write(f"- {exercise}")

    # Exercise Selection
    exercise = st.selectbox("Choose an exercise:", list(CBT_EXERCISES.keys()))

    if st.button("Start Exercise"):
        exercise_info = CBT_EXERCISES[exercise]
        st.write(f"### {exercise}")
        st.write(exercise_info["description"])
        st.write("### Steps:")
        for step in exercise_info["steps"]:
            st.write(step)
        
        # Journaling Input
        st.write("### Reflection/Journaling")
        journal_entry = st.text_area("Write your reflections after completing the exercise:")
        
        if st.button("Save Journal Entry"):
            # Here we would save the journal entry to a file or database
            st.success("Your journal entry has been saved!")

def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Chat", "CBT Exercises"])

    if page == "Chat":
        chat_page()
    elif page == "CBT Exercises":
        cbt_exercise_page()

if __name__ == "__main__":
    main()
