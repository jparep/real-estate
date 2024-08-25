import pickle

# Load the pre-trained model from the file
model = pickle.load('models/house_price_model.pkl')

def predict_price(features):
    """Predict the house price based on the input features."""
    # Convert input data to the format expected by the model
    input_data = [float(features[key]) for key in features]
    prediction = model.predict([input_data])
    return round(prediction[0], 2)
