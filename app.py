#! /usr/bin python  
import time
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/hello")
def hello():
    return "Hello how are you"

if __name__ == "__main__": 
    app.run(host='127.0.0.1', port=5000)
 