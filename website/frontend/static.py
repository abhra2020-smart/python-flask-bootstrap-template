from flask import Blueprint, send_file

static = Blueprint('static', __name__)


@static.route('/static.js')
def js():
    return send_file("../frontend/templates/static/static.js")


@static.route('/static.css')
def css():
    return send_file("../frontend/templates/static/static.css")

