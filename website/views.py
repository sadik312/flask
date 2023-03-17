from flask import Blueprint

# define this file is a blueprint of app
views = Blueprint('views', __name__)

@views.route('/')
def home():
    return "<h1>Test</h1>"