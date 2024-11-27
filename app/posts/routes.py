from flask import render_template
from app.posts import bp

@bp.route('/')
def index():
    return "<h1>Flask Posts Route</h1>"