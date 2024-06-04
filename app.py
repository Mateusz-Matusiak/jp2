import sqlite3
from flask import Flask, render_template, request
from product import Product, Products

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/api', methods = ['GET'])
def index():
    conn = get_db_connection()
    store = conn.execute('SELECT * FROM store').fetchall()
    conn.close()
    products = []
    for product in store:
        products.append(Product(product['id'], product['product_name'],
                                product['quantity'], product['product_details']))
    products = Products(products)
    return products.toJSON()

@app.route('/api/add_product', methods=['GET', 'POST'])
def add_message():
    content = request.get_json(silent=True)
    product_data = content.get("product")
    product = Product(**product_data)
    conn = get_db_connection()
    cursor = conn.cursor()

    sqlite_insert_with_param = "INSERT INTO store (product_name, quantity, product_details) VALUES (?, ?, ?)"

    data_tuple = (product.product_name, product.quantity, product.product_details)
    cursor.execute(sqlite_insert_with_param, data_tuple)
    conn.commit()
    cursor.close()
    return "hello"


if __name__ == '__main__':
    app.run()