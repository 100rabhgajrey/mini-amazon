from amazon.models import db
import pymongo
from bson.objectid import  ObjectId

def get_details(p_id):
    cursor = db.products.find({'_id': ObjectId(p_id)})
    if cursor.count() == 1:
        return cursor[0]
    else:
        return None

def search_product(name):

    query = {'name': name}
    matching_products = db['products'].find(query)
    matching_products.sort([("price", pymongo.DESCENDING)])
    return list(matching_products)


def add_product(product):
    db['products'].insert_one(product)


def update_product(name, updated_product):
    filter = {'name': name}
    update = {
        '$set': updated_product
    }

    #Update in DB
    db['products'].update_one(filter=filter, update=update)
