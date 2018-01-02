from flask import Flask, render_template,redirect, url_for
import sqlite3

app = Flask(__name__)


@app.route("/")
def main():
    return render_template('index.html')

@app.route("/products")
def products():
    return render_template('products.html')

@app.route("/testimonials")
def testimonials():
    return render_template('testimonials.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route('/favicon.ico')
def favicon():
    return redirect(url_for('static', filename='images/favicon.ico'), code=302)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
