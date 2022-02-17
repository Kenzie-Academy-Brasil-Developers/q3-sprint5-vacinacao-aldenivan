from flask import Flask
from app.routes.vaccine_route import bp as bp_vaccine

def init_app(app: Flask):

    app.register_blueprint(bp_vaccine)