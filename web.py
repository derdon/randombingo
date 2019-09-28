import random

from flask import Flask, request, render_template, jsonify

from logic import grouper

app = Flask(__name__)
app.config.update(
    title='Random Bingo Generator',
    cols=5,
)


@app.route('/')
def index():
    return render_template('index.html', config=app.config)


@app.route('/custom', methods=['POST'])
def custom_bingo():
    values = request.form.getlist('values[]')
    filtered_values = list(filter(
        lambda value: value is not None and value.strip(), values))
    random.shuffle(filtered_values)
    num_cols = int(request.form['num_cols'])
    return jsonify(list(grouper(filtered_values, num_cols, '[BLANK]')))
