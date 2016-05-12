# -*- coding: utf-8 -*-

from echarts import Echart, Legend, Bar, Axis
from flask import Flask, jsonify
import functools
from gevent.pywsgi import WSGIServer


def create_app():
    app = Flask(__name__)


    def crossdomain(f):
        @functools.wraps(f)
        def wrapper(*args, **kwargs):
            resp = f(*args, **kwargs)
            h = resp.headers
            h['Access-Control-Allow-Origin'] = '*'
            h['Access-Control-Allow-Methods'] = 'GET'
            return resp
        return wrapper


    @app.route('/opt/bar')
    @crossdomain
    def bar():
        chart = Echart('GDP', 'This is a fake chart')
        chart.use(Bar('China', [2, 3, 4, 5]))
        chart.use(Legend(['GDP']))
        chart.use(Axis('category', 'bottom', data=['Nov', 'Dec', 'Jan', 'Feb']))
        return jsonify(chart.json)

    return app

if __name__ == '__main__':
    app = create_app()
    http_server = WSGIServer(('',5000), app)
    http_server.serve_forever()
