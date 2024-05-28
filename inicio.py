from flask import Flask, render_template, request, redirect, url_for, flash
import pymysql

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/perro')
def perro():
    return render_template("perro.html")

@app.route('/gatos')
def gatos():
    return render_template("gatos.html")

@app.route('/index')
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
