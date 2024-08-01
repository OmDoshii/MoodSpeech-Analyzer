
import speech_recognition as sr
from transformers import pipeline
import streamlit as st
import pandas as pd
import time

# Initialize the recognizer and the emotion classifier
recognizer = sr.Recognizer()
emotion_classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", return_all_scores=True)

# Function to analyze emotions
def analyze_emotion(text):
    result = emotion_classifier(text)
    return result

# Function to map emotions to emojis
def get_emoji(emotion):
    emoji_map = {
        "anger": "😠",
        "joy": "😊",
        "sadness": "😢",
        "surprise": "😲",
        "disgust": "🤢",
        "fear": "😨",
        "neutral": "😐"
    }
    return emoji_map.get(emotion, "")

# Streamlit App
def main():
    st.title("Speech to Emotion Analysis")

    # Initialize session state
    if 'listening' not in st.session_state:
        st.session_state.listening = False

    if 'data' not in st.session_state:
        st.session_state.data = []

    # Start/Finish buttons side by side
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Start Listening"):
            st.session_state.listening = True

    with col2:
        if st.button("Finish Listening"):
            st.session_state.listening = False

    # Loop to keep listening and analyzing until the user hits "Finish Listening"
    while st.session_state.listening:
        with sr.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.1)
            st.write("Listening...")
            audio = recognizer.listen(mic)

            try:
                text = recognizer.recognize_google(audio_data=audio)
                st.write("Recognized Text: " + text)

                emotions = analyze_emotion(text)
                best_emotion = max(emotions[0], key=lambda e: e['score'])
                st.write(f"Recognized Emotion: {best_emotion['label']} {get_emoji(best_emotion['label'])} - Score: {best_emotion['score']:.4f}")

                # Save data
                st.session_state.data.append([text, best_emotion['label']])

            except sr.UnknownValueError:
                st.write("Could not understand audio")
            except sr.RequestError as e:
                st.write(f"Could not request results; {e}")

        # Wait for 5 seconds before continuing
        time.sleep(5)
        st.experimental_rerun()

    # Show Database button after recognized emotions and scores
    if st.button("Show Database"):
        st.session_state.listening = False
        df = pd.DataFrame(st.session_state.data, columns=['Review', 'Result'])
        df.to_excel("emotion_analysis.xlsx", index=False)
        st.write(df)
        st.write("Database saved as emotion_analysis.xlsx")

if __name__ == "__main__":
    main()
