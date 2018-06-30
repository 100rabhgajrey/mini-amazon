from amazon.models import db
from flask import render_template


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