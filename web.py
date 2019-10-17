import os
import os.path

from flask import Flask, request, render_template, jsonify
from werkzeug.utils import secure_filename

from logic import bingo_from_iterable

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'.txt', '.csv'}


app = Flask(__name__)
app.config.update(
    title='Random Bingo Generator',
    # limit upload size to 16 Megabyte
    MAX_CONTENT_LENGTH=16 * 1024 * 1024,
    UPLOAD_FOLDER=UPLOAD_FOLDER,
)


def allowed_file(filename):
    _, ext = os.path.splitext(filename)
    return '.' in filename and ext.lower() in ALLOWED_EXTENSIONS


@app.route('/')
def index():
    return render_template('index.html', config=app.config)


@app.route('/custom', methods=['POST'])
def custom_bingo():
    values = request.form.getlist('values[]')
    return jsonify(list(bingo_from_iterable(values)))


@app.route('/file-upload', methods=['POST'])
def bingo_by_uploaded_file():
    file = request.files['file']
    if file.filename == '':
        return ''
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        abs_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(abs_path)
        with open(abs_path) as fp:
            values = bingo_from_iterable(fp)
        # remove the file from upload directory again, don't store it
        os.remove(abs_path)
        return jsonify(list(values))
    return jsonify([])
