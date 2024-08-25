from flask import Blueprint, render_template, request
from .models import predict_price

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = request.form.to_dict()
        prediction = predict_price(data)
        return render_template('result.html', prediction=prediction)
    return render_template('index.html')
