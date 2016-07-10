from flask import request, url_for
from userv.encyclopedia.models import Fact
from pprint import pprint
from datetime import datetime, timezone
import arrow

import json


def test_factoids_all_one(session, db,app, client):

    now = datetime.now(timezone.utc)
    anow = arrow.get(now)
    f = Fact(id=1, name='foo', author='Ben Franklin', popularity=42,
            value="don't panic", added=now)

    session.add(f)

    #session.commit()

    print(client.get('/api/v1/factoids/all').get_data())
    response = client.get(url_for('encyclopedia.factoidsall')).json
    
    expected = [
                {'id': 1,
                 'name': 'foo',
                 'author': 'Ben Franklin',
                 'popularity': 42,
                 'value': "don't panic",
                 'added': str(anow)
                 }
                ]
    assert response == expected

def test_factoids_all_many(session, db,app, client):

    now = datetime.now(timezone.utc)
    anow = arrow.get(now)
    f = Fact(id=1, name='foo', author='Ben Franklin', popularity=42,
            value="don't panic", added=now)
    session.add(f)

    f = Fact(id=2, name='bar', author='Alexander Hamilton', popularity=-1,
            value='I am not giving away my shot', added=now)
    session.add(f)

    print(client.get('/api/v1/factoids/all').get_data())
    response = client.get(url_for('encyclopedia.factoidsall')).json
    
    expected = [
                {'id': 1,
                 'name': 'foo',
                 'author': 'Ben Franklin',
                 'popularity': 42,
                 'value': "don't panic",
                 'added': str(anow)
                 },
                {'id': 2,
                  'name': 'bar',
                  'author': 'Alexander Hamilton',
                  'popularity': -1,
                  'value': 'I am not giving away my shot',
                  'added': str(anow)
                }
                ]


    assert response == expected


def test_factoid_one(session, client):

    now = datetime.now(timezone.utc)
    anow = arrow.get(now)
    f = Fact(id=1, name='foo', author='Ben Franklin', popularity=42,
            value="don't panic", added=now)

    session.add(f)

    #session.commit()

    print(client.get('/api/v1/factoids/fact/foo').get_data())
    response = client.get(url_for('encyclopedia.factoidbyname', name='foo')).json
    
    expected =  {'id': 1,
                 'name': 'foo',
                 'author': 'Ben Franklin',
                 'popularity': 42,
                 'value': "don't panic",
                 'added': str(anow)
                 }
                
    assert response == expected

