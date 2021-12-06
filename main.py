import os

from flask import Flask, redirect


TO_REDIRECT = os.environ.get('TO_REDIRECT')

app = Flask(__name__)


@app.route('/')
def main():
   return redirect(TO_REDIRECT)

