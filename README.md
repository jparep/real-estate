# House Price Prediction API

This project is a Flask-based API for predicting house prices using a machine learning model. The API allows users to input house features and receive a predicted price in response.

## Table of Contents

- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Model Training](#model-training)
- [Testing](#testing)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

These instructions will guide you through setting up and running the Flask API on your local machine for development and testing purposes.

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Virtualenv (optional but recommended)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/house-price-prediction-api.git
   cd house-price-prediction-api

2. **Create and activate a virtual environment:**
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. **Install the required Python packages:**
```bash
pip install -r requirements.txt
```

4. **Install Tailwind CSS dependencies:**
```bash
npm install
```

5. **Build Tailwind CSS:**
```bash
npx tailwindcss -i ./app/static/css/tailwind.css -o ./app/static/css/output.css --minify
```

6. **Set up the environment variables:**

Create a .env file in the root directory and add your configuration settings, such as:

```bash
npx tailwindcss -i ./app/static/css/tailwind.css -o ./app/static/css/output.css --minify
```

# Project Structure
house-price-prediction/
├── app/
│   ├── __init__.py                # Initializes Flask application
│   ├── routes.py                  # Defines API routes and views
│   ├── models.py                  # Handles loading and using the pre-trained ML model
│   ├── forms.py                   # Manages forms (if any)
│   ├── static/                    # Static files (CSS, JS, images)
│   │   ├── css/
│   │   │   └── tailwind.css       # Tailwind CSS styles
│   │   └── js/
│   └── templates/                 # HTML templates for rendering views
│       ├── index.html             # Home page with prediction form
│       └── result.html            # Displays prediction results
├── data/
│   └── house_data.csv             # Training and testing data (optional)
├── models/
│   └── house_price_model.pkl      # Pre-trained machine learning model
├── tests/
│   ├── test_routes.py             # Tests for API routes
│   └── test_models.py             # Tests for model loading and prediction
├── .env                           # Environment variables
├── .gitignore                     # Files to be ignored by Git
├── config.py                      # Configuration settings for the app
├── Dockerfile                     # Dockerfile for containerizing the app
├── docker-compose.yml             # Docker Compose for multi-container setup
├── requirements.txt               # Python dependencies
├── tailwind.config.js             # Tailwind CSS configuration
└── wsgi.py                        # WSGI entry point for production

# Usage

1. **Run the Flask application:**
```bash
flask run
```

2. **Access the API:**

Open your browser or use a tool like curl or Postman to interact with the API at:
```bash
http://127.0.0.1:5000/
```

# API Endpoints 

POST /predict

Predict the house price based on the provided features.

    Request: JSON object containing the house features.

# Model Training

To retrain the model with new data:

    Add your training data to the data/ directory.
    Create a new training script or use the existing one to train the model.
    Save the trained model to the models/ directory.


#Testing

To run tests, you can use Python's unittest or pytest.

Example with pytest:
```bash
pytest tests/
```

# Deployment
Dockerization

1. **Build the Docker image:**

```bash 
    docker build -t house-price-prediction-api .
```

2. **Run the Docker container:**
```bash
docker run -p 5000:5000 house-price-prediction-api
```

3. **Using Docker Compose:**

```bash
docker-compose up --build
```

# Deployment to Cloud (e.g., Heroku, AWS, GCP)

1. **Deploy to Heroku**
```bash
heroku container:push web --app your-app-name
heroku container:release web --app your-app-name
```

2. **Deploy to AWS/GCP:**

    Use AWS Elastic Beanstalk or GCP Cloud Run to deploy your Dockerized application.
    Ensure that environment variables and configurations are set according to your cloud provider's requirements.


# Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes. Ensure that your code follows best practices and is well-documented


# License

This project is licensed under the MIT License. See the LICENSE file for details.