from flask import Flask
from .database import db




def create_app(name, config=None, app_override=None):
    app = Flask(name)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    if config:
        app.config.update(config)
        
    db.init_app(app)
    db.app = app
    with app.app_context():
        from . import encyclopedia
    
        app.register_blueprint(encyclopedia)
        db.create_all()
        return app
