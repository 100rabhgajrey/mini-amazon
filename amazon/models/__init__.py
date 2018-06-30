from pymongo import MongoClient


# connect to mongodb server
client = MongoClient('localhost', 27017)
# select pymlb2-amazon database
db = client['mini-amazon']
