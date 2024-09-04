from flask import Flask
from flask_pymongo import PyMongo
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/finance-manager'
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'

mongo = PyMongo(app)
jwt = JWTManager(app)

from routes import user_routes, transaction_routes

app.register_blueprint(user_routes.bp)
app.register_blueprint(transaction_routes.bp)

if __name__ == '__main__':
    app.run(debug=True)
