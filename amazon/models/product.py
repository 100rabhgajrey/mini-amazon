from amazon.models import db
import pymongo
from bson.objectid import  ObjectId

def get_details(p_id):
    cursor = db.products.find({'_id': ObjectId(p_id)})
    if cursor.count() == 1:
        return cursor[0]
    else:
        return None

def search_by_name(name):

    query = {'name': name}
    matching_products = db['products'].find(query)
    matching_products.sort([("price", pymongo.DESCENDING)])
    return list(matching_products)


def add_product(product):
    db['products'].insert_one(product)


def update_products(p_id, updated_product):
    condition = {'_id': ObjectId(p_id)}
    cursor = db.products.find(condition)

    if cursor.count() == 1:
        update = {
            '$set': updated_product
        }
    else:
        return None
        # update in DB


    db['products'].update_one(filter=condition, update=update, upsert=True)

def delete_products(p_id):
    condition = {'_id': ObjectId(p_id)}
    cursor = db.products.find(condition)

    if cursor.count() == 1:
        product_data = cursor[0]
    else:
        return False

    db['products'].remove(product_data)
    db.users.update_one(filter=condition, update={'$set': product_data})
    return True