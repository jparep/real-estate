import joblib

model = joblib.load('models/model.joblib')

def predict_price(features):
    # Convert input data to the format expected by the model
    input_data = [float(features[key]) for key in features]
    prediction = model.predict([input_data])
    return round(prediction[0], 2)