from flask import Flask
from flask import app

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello Puppy!</h1>"

if __name__ == '__main__':
    app.run()