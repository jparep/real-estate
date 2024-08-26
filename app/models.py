import joblib

# Load the pre-trained model from the file
with open('models/model.joblib', 'rb') as model_file:
    model = joblib.load(model_file)

def predict_price(features):
    """Predict the house price based on the input features."""
    try:
        # Extract and convert the input data to the format expected by the model
        input_data = [
            float(features['Avg. Area Income']),
            float(features['Avg. Area House Age']),
            float(features['Avg. Area Number of Rooms']),
            float(features['Avg. Area Number of Bedrooms']),
            float(features['Area Population'])
        ]
        prediction = model.predict([input_data])
        return round(prediction[0], 2)
    except KeyError as e:
        raise ValueError(f"Missing key in input features: {e}")
    except ValueError as e:
        raise ValueError(f"Invalid value in input features: {e}")

