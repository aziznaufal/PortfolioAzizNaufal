from flask import Blueprint
from controller.weather_controller import index

weather_bp = Blueprint('weather', __name__)
weather_bp.route('/', methods=['GET', 'POST'])(index)

