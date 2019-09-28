import random

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
    n = int(request.form['num_cols'])
    return jsonify(list(grouper(generate_words(count), n)))


@app.route('/custom', methods=['POST'])
def custom_bingo():
    values = request.form.getlist('values[]')
    filtered_values = list(filter(
        lambda value: value is not None and value.strip(), values))
    # TODO: add values from values until the desired size is reached (i.e. 25)
    random.shuffle(filtered_values)
    num_cols = int(request.form['num_cols'])
    return jsonify(list(grouper(filtered_values, num_cols)))
