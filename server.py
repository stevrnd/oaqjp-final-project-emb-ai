"""
This module provides a Flask application for Emotion Detection.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_predictor

app = Flask("Emotion Detection")

@app.route("/")
def render_index_page():
    """
    Renders the index page.
    """
    return render_template('index.html')

@app.route("/emotionDetector")
def emotion_det():
    """
    Handles the emotion detection route.
    """
    text_to_analyze = request.args.get('textToAnalyze')  # Fixed the argument name
    response = emotion_predictor(text_to_analyze)
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again."

    # Extracting emotions from the response dictionary
    anger, disgust, fear, joy, sadness = (
        response.get('anger', 0),
        response.get('disgust', 0),
        response.get('fear', 0),
        response.get('joy', 0),
        response.get('sadness', 0)
    )

    dominant_emotion = response['dominant_emotion']

    result_message = (
        f"For the given statement, the system response is {anger}, {disgust}, {fear}, {joy}, \
         and {sadness}. "
        f"The dominant emotion is {dominant_emotion}"
    )

    return result_message

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
