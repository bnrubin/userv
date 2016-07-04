from flask import Flask, jsonify, Blueprint, current_app
from flask_sqlalchemy import SQLAlchemy

from userv.encyclopedia.models import Fact
from userv.encyclopedia.schemas import fact_schema

encyclopedia = Blueprint('encyclopedia', __name__, url_prefix='/api/v1/factoids/')

@encyclopedia.route('all')
def all():
    factoids = Fact.query.all()
    return jsonify(fact_schema.dump(factoids).data)
