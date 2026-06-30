from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import os
import numpy as np

# This is the step where the web server app is actually created
app = Flask(__name__)
CORS(app) 

# Loading model (brain)
model = joblib.load('student_performance_model.pkl')

# Telling about address
@app.route('/predict', methods=['POST'])
# Defining function
def predict():
    try:
        data = request.json
        hours = float(data.get('Hours Studied', 0))
        scores = float(data.get('Previous Scores', 0))
        sleep = float(data.get('Sleep Hours', 0))
        papers = float(data.get('Sample Question Papers Practiced', 0))
        
        features = np.array([[hours, scores, sleep, papers]])
        prediction = model.predict(features)[0]
        
        return jsonify({
            'success': True,
            'prediction': round(prediction, 2)
        })
        
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)