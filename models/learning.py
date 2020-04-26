from flask import Blueprint
l_b = Blueprint('learning',__name__)

@l_b.route('<string:name>')
def home(name):
    return f"Hello, {name}"