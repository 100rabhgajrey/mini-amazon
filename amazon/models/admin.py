from amazon.models import db


def __search_by_admin_name(username):
    query={'username': username}
    matching_user = db['users'].find(query)
    if matching_user.count() > 0:
        return matching_user.next()
    else:
        return None