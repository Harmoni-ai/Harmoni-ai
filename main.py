import streamlit as st
from src.bot import TherapyBot
from config import GROQ_API_KEY, MODEL_NAME, TEMPERATURE
from src.cbt_exercises import CBT_EXERCISES, get_personalized_exercises

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

    # User input
    prompt = st.chat_input("How are you feeling today?")

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
