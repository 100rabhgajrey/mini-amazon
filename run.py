from flask import Flask, request, send_from_directory, jsonify

app = Flask('Amazon')

products = []


@app.route('/', methods=['GET'])
def index():
    return send_from_directory('static', 'index.html')


@app.route('/api/product', methods=['GET', 'POST'])
def product():
    if request.method == 'GET':
        query = request.args['name']
        for prod in products:
            if prod['name'] == query:
                return jsonify(prod)
        return 'No match'
    elif request.method == 'POST':
        op_type = request.form['op_type']
        name = request.form['name']
        desc = request.form['desc']
        price = request.form['price']
        if op_type == 'add':
            prod = {
                'name': name,
                'desc':  desc,
                'price': price
            }
            products.append(prod)
            return send_from_directory('static', 'index.html')
        elif op_type == 'update':
            for prod in products:
                if prod['name'] == name:
                    prod['desc'] = desc
                    prod['price'] = price
                    return send_from_directory('static', 'index.html')
            return 'product not found'


if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5005, debug=True)

