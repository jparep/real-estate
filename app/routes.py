from flask import Blueprint, render_template, request
from .models import model

mian = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
