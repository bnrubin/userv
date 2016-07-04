from flask import Flask
from flask_sqlalchemy import SQLAlchemy

def create_app(name, config=None):
    app = Flask(name)
    if config:
        app.config.update(config)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'

    from userv.encyclopedia import encyclopedia
    app.register_blueprint(encyclopedia)
    
    from userv.encyclopedia.models import db

    db.init_app(app)

    with app.app_context():
        db.create_all()

    return app
