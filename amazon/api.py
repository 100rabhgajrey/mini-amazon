from flask import request, render_template,send_from_directory
from pymongo import MongoClient
from amazon import app

# connect to mongodb server
client = MongoClient('localhost', 27017)
# select pymlb2-amazon database
db = client['pymlb2-amazon']


@app.route('/', methods=['GET'])
def index():
    return send_from_directory('./amazon/static', 'index.html')


@app.route('/api/product', methods=['GET', 'POST'])
def product():
    if request.method == 'GET':
        # lets search for the product here
        query = {'name': request.args['name']}
        matching_products = db['products'].find(query)

        # return the first matching product
        return render_template('results.html',
                               query=query['name'],
                               results=list(matching_products))
    elif request.method == 'POST':
        # lets add and update here
        op_type = request.form['op_type']

        # read data from request and store in a dict
        prod = {
            'name': request.form['name'],
            'desc': request.form['desc'],
            'price': request.form['price']
        }

        if op_type == 'add':  # add the product here
            # insert to DB
            db['products'].insert_one(prod)

            # take user back to index page
            return send_from_directory('./amazon/static', 'index.html')

        elif op_type == 'update':  # update the product here
            # create filter and update dicts
            filter = {'name': request.form['name']}
            update = {
                '$set': prod
            }

            # update in DB
            db['products'].update_one(filter=filter, update=update)

            # take user back to index page
            return send_from_directory('./amazon/static', 'index.html')
