from flask import Flask
from . import views

def create_app() -> None:
    app = Flask(__name__)
    views.init_app(app)
    
    return app