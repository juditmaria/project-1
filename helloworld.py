from flask import Flask, render_template

app = Flask(__name__)

@app.route("/hello/")

def hello_world():
    return render_template('helloworld.html')