import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():    
    return "Welcome! this is flask-app port 2000"

@app.route('/how are you')
def hello():
    return 'I am  good, how about you?'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
