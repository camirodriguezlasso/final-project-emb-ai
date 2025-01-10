from flask import Flask, request, jsonify
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector', methods=['POST'])
def emotion_detector_route():
    
    data = request.get_json()
    text_to_analyze = data.get("text", "")

    emotion_results = emotion_detector(text_to_analyze)

    response = {
        "anger": emotion_results['anger'],
        "disgust": emotion_results['disgust'],
        "fear": emotion_results['fear'],
        "joy": emotion_results['joy'],
        "sadness": emotion_results['sadness'],
        "dominant_emotion": emotion_results['dominant_emotion']
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
