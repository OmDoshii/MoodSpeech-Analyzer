SpeechMood Analyzer App
Description
SpeechMood Analyzer is an interactive real-time application that leverages machine learning to recognize emotions from spoken language. Utilizing speech recognition and emotion analysis models, the application processes audio input from a microphone, transcribes it into text, and determines the predominant emotion conveyed. SpeechMood Analyzer can recognize a range of emotions, including anger, joy, sadness, surprise, disgust, fear, and neutrality. This project demonstrates the integration of speech recognition and natural language processing for emotion analysis, which can be beneficial for various applications, including customer service, mental health monitoring, and user experience enhancement.

Why is it Important?
Understanding human emotions in spoken language is critical for improving human-computer interactions, sentiment analysis, and mental health monitoring. SpeechMood Analyzer provides a simple and interactive way to showcase the capabilities of emotion detection from speech. It can serve as a foundation for developing more advanced applications or as an educational tool in the fields of speech recognition and natural language processing.

How to Use
To use the SpeechMood Analyzer App:

Ensure you have Python installed on your system.
Install the required libraries by running pip install -r requirements.txt.
Run the application using streamlit run app.py.
The application will open in your web browser. Click the "Start Listening" button to begin recognizing speech and emotions in real-time. Click the "Finish Listening" button to stop the process, and click the "Show Database" button to display and save the recorded data to an Excel file.
Technologies Used
SpeechRecognition: Library for converting spoken language into text.
Transformers: Hugging Face's library for natural language processing models.
Streamlit: Web application framework for creating interactive web applications with Python.
Pandas: Data manipulation library for handling and saving data to Excel files.
PyAudio: Library for capturing audio input from the microphone.
Documentation
Project Structure
The project structure is organized as follows:

app.py: Main script to run the SpeechMood Analyzer App.
requirements.txt: List of required Python libraries.
README.md: Project documentation file.
Functionality
1. Speech Recognition and Emotion Analysis
The application captures audio input using the microphone, transcribes it to text, and analyzes the text to detect the predominant emotion. The emotion analysis is performed using a pre-trained model from Hugging Face's Transformers library.

2. Streamlit Application
The Streamlit application is initialized to configure the layout, display controls for starting and stopping the speech recognition process, and provide a button to display and save the recorded data.

3. Real-time Speech to Emotion Recognition
The main loop captures audio input, processes it, and uses the emotion detection model to predict the emotion of the recognized text. The detected emotion is then displayed in real-time, along with the corresponding emoji.

4. Data Recording and Export
The application records the recognized text and corresponding emotions in a session state. When the user hits the "Show Database" button, the recorded data is saved to an Excel file and displayed in the application.

Usage
Run the application using streamlit run app.py.
Click the "Start Listening" button to begin the real-time speech-to-emotion recognition.
Speak into the microphone and observe the recognized text and detected emotions.
Click the "Finish Listening" button to stop the process.
Click the "Show Database" button to display and save the recorded data to an Excel file.
View the saved data in the generated Excel file named emotion_analysis.xlsx.