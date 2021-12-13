import os

os.environ['TO_REDIRECT'] = 'https://example.com'

import pytest

from main import app


app.config['TESTING'] = True


def test_redirect(monkeypatch):
    client = app.test_client() 
    resp = client.get('/')
    assert resp.status_code == 302
    assert resp.headers['location'] == 'https://example.com/'

def test_redirect_with_path(monkeypatch):
    client = app.test_client() 
    resp = client.get('/hoge/fuga')
    assert resp.status_code == 302
    assert resp.headers['location'] == 'https://example.com/hoge/fuga'
