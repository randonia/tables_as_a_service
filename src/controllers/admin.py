from time import time

from elasticsearch import Elasticsearch
from flask import (abort, request, g)

from app import app
import tablr
from views.root import *


### Command and Control API points
@app.route('/admin/reset')
def reset_database():
    if g.auth:
        start_time = time()
        print 'Resetting database - Request from %s' % request.remote_addr
        reset_emoji_db()
        end_time = time()
        return render_status(200, 'Database reset',
                             {'took': round(end_time - start_time, 2)})
    abort(403)


def reset_emoji_db():
    tablr.load_tables()
