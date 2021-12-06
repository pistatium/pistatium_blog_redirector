import os

from flask import Flask, redirect


TO_REDIRECT = os.environ.get('TO_REDIRECT')

app = Flask(__name__)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def redirector(path: str):
   return redirect(f'{TO_REDIRECT}/{path}', code=301)

