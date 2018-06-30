from amazon.models import db

def search_product(name):

    query = {'name': name}
    matching_products = db['products'].find(query)
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
