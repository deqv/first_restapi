from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList
from db import db

from security import authenticate, identity

# Below the app is created
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.secret_key = 'superlongandsecurepassword'
# Below the api is created and imported from flask_restful
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

#JWT creates a new endpoint /auth, which intakes a username and password.
# JWT then sends the username and password to the authenticate and identity functions
jwt = JWT(app, authenticate, identity)

# Below tells the api that the resource
# (eg: item/<string:name>) is now accessible via the api
api.add_resource(Item, '/item/<string:name>')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)
