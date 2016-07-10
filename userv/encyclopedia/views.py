from flask import Flask, jsonify, Blueprint, current_app
from flask_restful import Resource, Api
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound

from pprint import pprint

from . import api, db 

from .models import Fact
from .schemas import FactSchema

fact_schema = FactSchema()

class FactoidsAll(Resource):
    def get(self):
        factoids = Fact.query.all()
        return jsonify([fact_schema.dump(f).data for f in factoids])

class FactoidByName(Resource):
    def get(self, name):
        try:
            factoid = Fact.query.filter_by(name=name).one()
        except NoResultFound:
            return jsonify({'error': 'factoid not found'})
        except MultipleResultsFound:
            return jsonify({'error': "this shouldn't happen, multiple results found."})
        

        return jsonify(fact_schema.dump(factoid).data)



        
# appended to blueprint url_prefix: /api/v1/factoids/
api.add_resource(FactoidsAll, 'all')
api.add_resource(FactoidByName, 'fact/<string:name>')
