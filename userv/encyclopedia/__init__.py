from flask import Blueprint
from flask_restful import Api
from .database import db

encyclopedia = Blueprint('encyclopedia', __name__, url_prefix='/api/v1/factoids/')
api = Api(encyclopedia)
from . import views

