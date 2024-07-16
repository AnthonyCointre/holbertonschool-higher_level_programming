"""
Building on the previous exercise, add the functionality to fetch and display
data from a SQLite database in the Flask application.
The application should allow users to choose between JSON, CSV, and
SQL (SQLite database) as data sources using the source query parameter.
"""

from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/items')
def items():
    try:
        json_file_path = 'items.json'
        with open(json_file_path) as file:
            data = json.load(file)
            items = data.get("items", [])
    except FileNotFoundError:
        items = []
    return render_template('items.html', items=items)


@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)
    products = []
    error = None

    if source == 'json':
        try:
            with open('products.json') as file:
                products = json.load(file)
        except FileNotFoundError:
            error = "JSON file not found."
    elif source == 'csv':
        try:
            with open('products.csv') as file:
                reader = csv.DictReader(file)
                products = [row for row in reader]
                for product in products:
                    product['id'] = int(product['id'])
                    product['price'] = float(product['price'])
        except FileNotFoundError:
            error = "CSV file not found."
    elif source == 'sql':
        try:
            conn = sqlite3.connect('products.db')
            cursor = conn.cursor()
            if product_id:
                cursor.execute(
                    "SELECT * FROM Products WHERE id = ?", (product_id,))
            else:
                cursor.execute("SELECT * FROM Products")
            rows = cursor.fetchall()
            products = [{"id": row[0], "name": row[1],
                         "category": row[2], "price": row[3]} for row in rows]
            conn.close()
        except sqlite3.Error as e:
            error = f"Database error: {e}"
    else:
        error = "Wrong source parameter. Use 'json', 'csv', or 'sql'."

    if product_id and not products:
        error = "Product not found."

    return render_template('product_display.html', products=products, error=error)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
