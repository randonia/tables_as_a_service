import json
import os
from random import randint as rnd

from elasticsearch import Elasticsearch
from flask import (abort, request, g, send_from_directory)

from app import app
import tablr
from views.root import *

config = {}


@app.before_first_request
def initialize():
    load_config()


def load_config():
    tokens_file = open('authorized_users.json', 'r')
    tokens = json.load(tokens_file)
    config['AUTHORIZED_TOKENS'] = tokens


@app.before_request
def before_request():
    g.es = Elasticsearch()
    g.auth = user_authorized(request.headers.get('DongrAuth', None))


def user_authorized(token):
    if '/admin/' in request.path and token is None:
        abort(403)
    # Check token here
    return token in map(lambda entry: entry['token'],
                        config['AUTHORIZED_TOKENS']['admin'])


def get_user_by_token(token):
    return


@app.teardown_request
def teardown_request(exception):
    pass


@app.route('/favicon.ico')
def favicon():
    return send_from_directory('static', 'favicon.ico')


### API
@app.route('/')
def root():
    g.url = request.url_root
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


@app.route('/dongers/rand')
def donger_random():
    count = rnd(0, g.es.count(index='emoji', q='key:random')['count'] - 1)
    result = g.es.search(index='emoji', q='key:random', from_=count, size=1)
    return render_response(result)
