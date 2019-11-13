from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os
import requests
from walrus import *
# import simplejson
# import json
#Init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

#Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# Init db
db = SQLAlchemy(app)
# cache = Cache(db)
dba = Database()
cache = dba.cache()
# Init ma
ma = Marshmallow(app)


# Product Class/Model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(200))
    price = db.Column(db.Float)
    qty = db.Column(db.Integer)

    def __init__(self, name, description, price, qty):
        self.name = name
        self.description = description
        self.price = price
        self.qty = qty


# Product Schema
class ProductSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'description', 'price', 'qty')


# Init Schema
product_schema = ProductSchema(strict=True)
products_schema = ProductSchema(many=True, strict=True)


# Create a Product
@app.route('/product', methods=['POST'])
def add_product():
    name = request.json['name']
    description = request.json['description']
    price = request.json['price']
    qty = request.json['qty']

    new_product = Product(name, description, price, qty)

    db.session.add(new_product)
    db.session.commit()

    return product_schema.jsonify(new_product)


# Get all products
@app.route('/product', methods=['GET'])
def get_products():
    all_products = Product.query.all()
    result = products_schema.dump(all_products)
    return jsonify(result.data)


# Get single product
@app.route('/product/<id>', methods=['GET'])
def get_product(id):
    product = Product.query.get(id)
    return product_schema.jsonify(product)

# Update a Product
@app.route('/product/<id>', methods=['PUT'])
def update_product(id):
    product = Product.query.get(id)

    name = request.json['name']
    description = request.json['description']
    price = request.json['price']
    qty = request.json['qty']

    product.name = name
    product.description = description
    product.price = price
    product.qty = qty

    db.session.commit()

    return product_schema.jsonify(product)

# Delete product
@app.route('/product/<id>', methods=['DELETE'])
def delete_product(id):
    product = Product.query.get(id)
    db.session.delete(product)
    db.session.commit()

    return product_schema.jsonify(product)


@app.route('/', methods=['GET'])
# @Cache.cached(Cache, timeout=60)
# @cache.cached(timeout=30)
def computation_task():
    for i in range(1, 10000):
        res = 0
        result = 0
        for j in range(1, 1000):
            res = res + j
            result = j + j
    return render_template('index.html', sum=res)


@app.route('/data', methods=['GET'])
def data_api():
    requests.get("http://dummy.restapiexample.com/api/v1/employees")
    requests.get("http://dummy.restapiexample.com/api/v1/employees")
    requests.get("http://dummy.restapiexample.com/api/v1/employees")
    requests.get("http://dummy.restapiexample.com/api/v1/employees")
    requests.get("http://dummy.restapiexample.com/api/v1/employees")
    requests.get("http://dummy.restapiexample.com/api/v1/employees")
    requests.get("http://dummy.restapiexample.com/api/v1/employees")
    requests.get("http://dummy.restapiexample.com/api/v1/employees")
    return "Hello"
    #
    # r = requests.get("http://dummy.restapiexample.com/api/v1/employees")
    # for i in range(1, 5):
    #     list_data = r.json()
    #     for z in range(8):
    #         list_data.extend(list_data)
    #     # data = jsonify(r.json())
    #     # print(r)
    #     # print(r.json())
    #
    #     count = 10
    #     for d in list_data:
    #         while count > 0:
    #             for k, v in d.items():
    #                 pass
    #             count = count - 1
    # # print(dict_data)
    # data = jsonify(list_data)
    # return data


@app.route('/list_data', methods=['GET'])
# @Cache.cached(Cache, timeout=60)
def new_api():
    # r = requests.get("http://dummy.restapiexample.com/api/v1/employees")
    # list_data = r.json()
    # for num in range(0, 8):
    #     list_data.extend(list_data)
    # print(len(list_data))
    # return "Hi"\

    # print(json.loads(response.text))
    # json_data = response.json() if response and response.status_code == 200 else None
    # print(jsonify(response.json()))
    # print(type(response.json()))
    # list_data = r.json()
    # print(type(list_data))
    # data = jsonify(list_data)
    # print(data)
    return jsonify(requests.get("https://jsonplaceholder.typicode.com/comments").json())


@app.route('/fibonacci', methods=['GET'])
def get_fibonacci():

    series_length = 10000
    first = 0
    second = 1
    fibonacci_list = []
    count = 0
    while count < series_length:
        fibonacci_list.append(first)
        third = first + second
        first = second
        second = third
        count = count + 1
    return render_template("index.html", series=fibonacci_list)


@app.route('/direct', methods=['GET'])
def hello_word():
    for i in range(1, 10000):
        res = 0
        result = 0
        for j in range(1, 1000):
            res = res + j
            result = j + j
    return render_template('index.html', sum=res)


# Run server
if __name__ == '__main__':
    app.run(debug=True)
