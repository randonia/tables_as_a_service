import os
from random import randint as rnd
import sys

from flask import (Flask, request, session, g, redirect, url_for, abort,
                   render_template, flash, jsonify as to_js)

ROOT_PATH = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.path.dirname(__file__))

# Setup the config
DEBUG = __name__ == '__main__'

TEMPLATES_DIR = '%s/templates' % ROOT_PATH
TABLES_DIR = '%s/tables' % ROOT_PATH


# Load the tables
def load_tables(root, fname):
    f = open(os.path.join(root, fname), 'r')
    data = [line.strip() for line in f.readlines()]
    f.close()
    return data

TABLE_FIXES = load_tables(TABLES_DIR, 'fixes')
TABLE_FLIPS = load_tables(TABLES_DIR, 'flips')

app = Flask(__name__, static_folder='static',
            static_url_path='' if DEBUG else '/static')

app.config.from_object(__name__)
app.debug = DEBUG


@app.before_request
def before_request():
    pass


@app.teardown_request
def teardown_request(exception):
    pass


### Views
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/tables/flip')
def table_flip():
    return TABLE_FLIPS[rnd(0, len(TABLE_FLIPS) - 1)]


@app.route('/tables/fix')
def table_fix():
    return TABLE_FIXES[rnd(0, len(TABLE_FIXES) - 1)]


if __name__ == '__main__':
    app.run(host='0.0.0.0')
