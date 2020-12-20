import sys
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('mainpage.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    processed_text = text.upper()

    if 'ignore-blank-lines' in request.form:
        processed_text = text.lower()
    if 'ignore-trailing-spaces' in request.form:
        processed_text = text.lower()

    return processed_text
