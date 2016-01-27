from flask import (request, g, render_template, jsonify as to_js)

__all__ = (
    'render_response',
    'view_index',
    )


### Views
def view_index():
    return render_template('home.html')


def render_response(result):
    """
    Receives an Elasticsearch hit, renders out a response
    """
    # This definitely needs to be less awful
    return result['hits']['hits'][0]['_source']['text']
