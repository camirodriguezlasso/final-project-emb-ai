from flask import Flask, request, jsonify, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/emotionDetector', methods=['POST'])
def emotion_detector_route():
    try: 
        data = request.json
        text_to_analyze = data.get("text", "")

        if not text_to_analyze:
            return jsonify({'error': 'No text provided'}), 400

        emotion_results = emotion_detector(text_to_analyze)

        if emotion_results['dominant_emotion'] is None:
            return jsonify({'message': 'Invalid text! Please try again!'}), 400

        response_text = (
            f"For the given statement, the system response is 'anger': {emotion_results['anger']}, "
            f"'disgust': {emotion_results['disgust']}, 'fear': {emotion_results['fear']}, "
            f"'joy': {emotion_results['joy']} and 'sadness': {emotion_results['sadness']}. "
            f"The dominant emotion is {emotion_results['dominant_emotion']}."
        )

        return jsonify({'response': response_text, **emotion_results})

    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
