
CBT_EXERCISES = {
    "Thought Record": {
        "description": "Identify negative thoughts and challenge them.",
        "steps": [
            "1. Write down a situation that caused you distress.",
            "2. Identify the thoughts that came to your mind.",
            "3. Challenge the negative thoughts with evidence.",
            "4. Write down a balanced thought.",
        ],
    },
    "Behavioral Activation": {
        "description": "Engage in activities that bring joy.",
        "steps": [
            "1. List activities you enjoy.",
            "2. Schedule time for these activities this week.",
            "3. Reflect on how these activities made you feel.",
        ],
    },
    "Coping Statements": {
        "description": "Develop positive statements to counter negative thoughts.",
        "steps": [
            "1. Identify a negative thought.",
            "2. Create a coping statement to counter this thought.",
            "3. Repeat this statement when you feel distressed.",
        ],
    },
}


def get_personalized_exercises(mood):
    if mood == "anxious":
        return ["Deep Breathing", "Mindfulness Meditation"]
    elif mood == "depressed":
        return ["Gratitude Journaling", "Cognitive Restructuring"]
    else:
        return ["Gratitude Journaling", "Cognitive Restructuring", "Cognitive Restructuring"]
