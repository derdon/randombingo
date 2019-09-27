import numpy as np
from flask import Flask, request, render_template, jsonify

from logic import generate_words, grouper

app = Flask(__name__)
app.config.update(
    title='Random Bingo Generator',
)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/getwords', methods=['POST'])
def get_words():
    count = int(request.form['count'])
    n = int(request.form['rows'])
    return jsonify(list(grouper(generate_words(count), n)))
