from amazon.models import db
from bson.objectid import ObjectId

def search_by_userid(user_id):
    # lets search for the user here
    query = {'_id': ObjectId(user_id)}
    matching_user = db['users'].find(query)
    if matching_user.count() == 1:
        return matching_user.next()
    else:
     return None




def search_a_user(username):
    query = {'username': username}
    matching_user = db['users'].find(query)
    if matching_user.count() > 0:
        return matching_user.next()
    else:
        return None


def user_signup(name, username, password):
    existing_user = search_a_user(username)
    if existing_user is not None:
        return False
    else:
        user = {
            'name': name,
            'username': username,
            'password': password
        }
        db['users'].insert_one(user)
        return True


def authenticate(username, password):
    user = search_a_user(username)

    if user is None:
        # user does not exist
        return False

    if user['password'] == password:
        # user exists and correct password
        return True
    else:
        # user exists but wrong password
     return False


def add_to_cart(user_id, product_id):
    condition = {'_id': ObjectId(user_id)}

    cursor = db.users.find(condition)

    if cursor.count() == 1:
        user_data = cursor[0]
    else:
        # user id does not exist
        return False

    # to support old users
    if 'cart' not in user_data:
        user_data['cart'] = []

    # add product only if it hasnt been added in the past
    if product_id not in user_data['cart']:
        user_data['cart'].append(product_id)
        db.users.update_one(filter=condition, update={'$set': user_data})

    return True


def delete_from_cart(user_id, product_id):
    # TODO
    pass

    # return all products in a users cart


def retrieve_cart(user_id):
    condition = {'_id': ObjectId(user_id)}

    cursor = db.users.find(condition)

    if cursor.count() == 1:
        user_data = cursor[0]
        return user_data['cart']
    else:
     return False
