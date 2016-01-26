import os
from random import randint as rnd

from elasticsearch import Elasticsearch
from flask import (request, g, send_from_directory)

__all__ = (
    'root',
    'table_flip',
    'table_fix'
    )

from app import app
import tablr
from views.root import *

config = {}


@app.before_first_request
def initialize():
    load_config()
    tablr.load_tables()


def load_config():
    pass


@app.before_request
def before_request():
    tablr.log_request(request)
    g.es = Elasticsearch()


@app.teardown_request
def teardown_request(exception):
    pass


@app.route('/favicon.ico')
def favicon():
    return send_from_directory('static', 'favicon.ico')


### API
@app.route('/')
def root():
    print 'hi'
    return view_index()


@app.route('/tables/flip')
def table_flip():
    count = rnd(0, g.es.count(index='emoji', q='key:flip')['count'] - 1)
    result = g.es.search(index='emoji', q='key:flip', from_=count, size=1)
    return render_response(result)


@app.route('/tables/fix')
def table_fix():
    count = rnd(0, g.es.count(index='emoji', q='key:fix')['count'] - 1)
    result = g.es.search(index='emoji', q='key:fix', from_=count, size=1)
    return render_response(result)
