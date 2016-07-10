from flask import Flask
from flask import _app_ctx_stack as stack
import pytest
from userv.encyclopedia.factory import create_app
from userv.encyclopedia.database import db as _db
import os
from flask_sqlalchemy import SignallingSession


TESTDB = 'test_project.db'
#TESTDB_PATH = "/tmp/{}".format(TESTDB)
TEST_DATABASE_URI = 'sqlite:////tmp/unittest.db'


@pytest.fixture(scope='session')
def app(request):
    """Session-wide test `Flask` application."""
    settings_override = {
        'TESTING': True,
        'SQLALCHEMY_DATABASE_URI': TEST_DATABASE_URI
    }
    app = create_app(__name__, settings_override)

    # Establish an application context before running the tests.
    ctx = app.app_context()
    ctx.push()

    def teardown():
        ctx.pop()

    request.addfinalizer(teardown)
    return app

@pytest.fixture(scope='session')
def db(app, request):
    """Session-wide test database."""
    #if os.path.exists(TESTDB_PATH):
    #    os.unlink(TESTDB_PATH)

    def teardown():
        _db.drop_all()
    
    _db.app = app


    request.addfinalizer(teardown)
    return _db
 

@pytest.fixture(scope='function')
def session(db, request):
    """Creates a new database session for a test."""
    connection = db.engine.connect()
    transaction = connection.begin()

    

    options = {'bind':connection, 'binds':{}}
    session = db.create_scoped_session(options=options)

    db.session = session

    print(db.session.registry)
    def teardown():
        transaction.rollback()
        connection.close()
        session.remove()

    request.addfinalizer(teardown)
    return session
