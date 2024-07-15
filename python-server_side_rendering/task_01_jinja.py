"""
Build a basic Flask application that serves a web page using a Jinja template.
You will create a simple HTML template that includes various elements like
headings, paragraphs, and lists, and learn how to render it as a web page
using Flask.
Additionally, you will learn to create reusable templates for headers and
footers to promote code reusability and consistency across multiple pages.
"""

from flask import Flask, render_template

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


if __name__ == '__main__':
    app.run(debug=True, port=5000)
