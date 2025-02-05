from flask import Flask

app = Flask(__name__)

@app.route("/")

def home():
    # Function that handles requests to the root URL
    return "Hello, World!"