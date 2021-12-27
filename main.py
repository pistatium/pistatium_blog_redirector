import os
import logging

from flask import Flask, request


TO_REDIRECT = os.environ.get('TO_REDIRECT')

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('redirector')

app = Flask(__name__)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def redirector(path: str):
    logger.info(f"ua: {request.headers.get('User-Agent')}")
    headers = {}
    headers['Cache-Control'] = 'public, max-age=1209600'   
    headers['Location'] = f'{TO_REDIRECT}/{path}'
    return "", 308, headers


