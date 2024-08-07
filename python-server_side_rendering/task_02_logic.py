"""
Enhance the Flask application by integrating dynamic content into the HTML
templates using Jinja's loop and conditional constructs.
Read a list of items from a JSON file and display them dynamically
on a web page.
"""

from flask import Flask, render_template
import json

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


if __name__ == '__main__':
    app.run(debug=True, port=5000)
