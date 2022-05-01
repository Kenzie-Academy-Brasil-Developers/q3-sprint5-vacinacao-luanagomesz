from flask import Flask
from app.routes.vacinnation import bp_vacinnation

def init_app(app: Flask):
    app.register_blueprint(bp_vacinnation)
