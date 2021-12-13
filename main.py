import os

from flask import Flask


TO_REDIRECT = os.environ.get('TO_REDIRECT')

app = Flask(__name__)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def redirector(path: str):
    headers = {}
    headers['Cache-Control'] = 'public, max-age=1209600'   
    headers['Location'] = f'{TO_REDIRECT}/{path}'
    return "", 302, headers


