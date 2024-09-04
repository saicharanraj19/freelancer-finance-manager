from flask_pymongo import PyMongo

mongo = PyMongo()

def get_transaction_collection():
    return mongo.db.transactions
