# Set up your imports here!
# import ...
from flask import Flask

app = Flask(__name__)

@app.route('/') # Fill this in!
def index():
    # Welcome Page
    # Create a generic welcome page.
    return "Oh hellow there."

@app.route('/puppy_latin/<name>') # Fill this in!
def puppylatin(name):
    if name[-1] != 'y':
        return f"Hello {name}y, you little fucker!"
    else:
        return f"Hello {name[:-1]}iful, you little fucker!"

    # This function will take in the name passed
    # and then use "puppy-latin" to convert it!

    # HINT: Use indexing and concatenation of strings
    # For Example: "hello"+" world" --> "hello world"

if __name__ == '__main__':
    # Fill me in!
    app.run(debug=True)
