from flask import Blueprint, render_template, request
from .models import model

mian = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = request.form.to_dict()
        prediction = model(data)
        return render_template('result.html')
    render_template('index.html')

