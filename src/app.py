import numpy as np
import cv2
from flask import Flask, request, jsonify
from deepface import DeepFace
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/analyze', methods=['POST'])
def analyze_emotion():
    if 'image' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['image']

    # Read image bytes and convert to NumPy array
    img_bytes = np.frombuffer(file.read(), np.uint8)
    img_np = cv2.imdecode(img_bytes, cv2.IMREAD_COLOR)

    try:
        result = DeepFace.analyze(img_np, actions=['emotion'], enforce_detection=False)
        dominant_emotion = result[0]['dominant_emotion']
        emotions = result[0]['emotion']
        emotions_python = {k: float(v) for k, v in emotions.items()}

        response = {
            'dominant_emotion': dominant_emotion,
            'emotion_scores': emotions_python
        }
        return jsonify(response)

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
