import os
import sys

from elasticsearch import Elasticsearch
from flask import (Flask, request, session, g, redirect, url_for, abort,
                   flash, jsonify as to_js)

from app import app
import controllers.api

ROOT_PATH = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.path.dirname(__file__))

# Setup the config
DEBUG = __name__ == '__main__'

app.debug = DEBUG

SEED_FILE = 'seed_data'
DATA_PATH = '%s/tables/%s' % (ROOT_PATH, SEED_FILE)
TEMPLATES_DIR = '%s/templates' % ROOT_PATH


# Load the tables
def load_tables():
    f = open(DATA_PATH, 'r')
    data = [line.strip() for line in f.readlines()]
    f.close()
    write_data_to_es(data)


def write_data_to_es(payload):
    print '%s lines' % len(payload)
    es = Elasticsearch()
    es.indices.delete(index='emoji', ignore=[404])
    for row in payload:
        packet = row.split(',')
        key = packet[0]
        text = packet[1]
        body = {
            'key': packet[0],
            'text': packet[1]
            }
        es.index(index='emoji', body=body, doc_type='emoji-type')


def list_routes():
    import urllib
    output = []
    for rule in app.url_map.iter_rules():
        output.append(rule)

    for line in sorted(output):
        print line


if __name__ == '__main__':
    list_routes()
    load_tables()
    app.run(host='0.0.0.0')
