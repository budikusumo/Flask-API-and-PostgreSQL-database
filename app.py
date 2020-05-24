from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from sqlalchemy_utils import database_exists
from sqlalchemy.engine.url import make_url
from db import db, ClientURI, setup_module

from security import authenticate, identity
from controllers.user import UserRegister
from controllers.agama import Agama

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = ClientURI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'jose'
api = Api(app)

@app.before_first_request
def create_tables():
    url = make_url(app.config['SQLALCHEMY_DATABASE_URI'])
    if not database_exists(url):
        setup_module()
    db.create_all()


jwt = JWT(app, authenticate, identity)  # /auth

api.add_resource(Agama, '/agama')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)