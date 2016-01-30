from flask import (request, g, render_template, jsonify as to_json)

__all__ = (
    'render_response',
    'render_status',
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


def render_status(status_code, message, opts={}):
    response = {'status': status_code, 'message': message}
    response.update(opts)
    return to_json(response)
