from flask import Flask, request, jsonify
import pandas as pd
from joblib import dump, load

from dummy_model import DummyModel

app = Flask(__name__)

# Mock model loading, replace with your actual model loading logic
# If the model doesn't exist, create a placeholder model for demonstration purposes
model_filename = "logestic_regression_model2.joblib"
try:
    model = load(filename=model_filename)
except FileNotFoundError:
    print(f"Model file '{model_filename}' not found. Creating a placeholder model.")
    model = None


@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get data from the request
        data = request.get_json()

        # Extract oxygen and pulse rate values from the received data
        user_oxygen = float(data['oxygen'])
        user_pulse_rate = float(data['pulse_rate'])

        # Create a DataFrame from the received data
        user_data = pd.DataFrame({'Oxygen': [user_oxygen], 'PulseRate': [user_pulse_rate]})

        # Make predictions using the loaded model
        # For demonstration purposes, return a constant value if the model is not loaded
        prediction = 42 if model is None else model.predict(user_data)

        # Return the prediction as a JSON response
        return jsonify({'prediction': prediction.tolist()})

    except Exception as e:
        return jsonify({'error': str(e)})


if __name__ == '__main__':
    # Mock model loading, replace with your actual model loading logic
    if model is None:
        print("Training a placeholder model.")
        # Assume training a simple model for demonstration purposes
        dummy_data = {'Oxygen': [1, 2, 3], 'PulseRate': [4, 5, 6]}
        dummy_labels = [0, 1, 0]
        model = DummyModel()
        model.fit(pd.DataFrame(dummy_data), dummy_labels)
        dump(model, filename=model_filename)

    app.run(host='192.168.196.152', debug=True)
