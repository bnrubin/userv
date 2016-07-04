from flask import request, url_for


def test_factoids_all(client):
    uri = client.get(url_for('encyclopedia.all'))
    assert uri.json == {}
