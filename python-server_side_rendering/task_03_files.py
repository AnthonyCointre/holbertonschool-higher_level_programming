"""
Build a feature in the Flask application to read and display product data from
two different data formats: JSON and CSV.
Create a single HTML template that can display data from either file type,
depending on a query parameter provided in the URL.
Add functionality to the Flask application to filter product data based on
an optional id query parameter.
Additionally, handle edge cases such as invalid source parameter values or
when the specified id is not found in the data.
"""

from flask import Flask, render_template, request
import json
import csv

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
    if source == 'json':
        file_path = 'products.json'
        try:
            with open(file_path) as file:
                products = json.load(file)
        except FileNotFoundError:
            return render_template(
                'product_display.html',
                error="JSON file not found."
            )
    elif source == 'csv':
        file_path = 'products.csv'
        try:
            with open(file_path) as file:
                reader = csv.DictReader(file)
                products = [row for row in reader]
                for product in products:
                    product['id'] = int(product['id'])
                    product['price'] = float(product['price'])
        except FileNotFoundError:
            return render_template(
                'product_display.html',
                error="CSV file not found."
            )
    else:
        return render_template(
            'product_display.html',
            error="Wrong source parameter. Use 'json' or 'csv'."
        )
    if product_id:
        products = [
            product for product in products if product['id'] == product_id]
        if not products:
            return render_template(
                'product_display.html',
                error="Product not found."
            )
    return render_template('product_display.html', products=products)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
