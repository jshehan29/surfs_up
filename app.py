# Import the flask dependency or library
from flask import Flask

# Create a new Flask app instance
app = Flask(__name__)

# Create Flask routes
@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/square')
def square():
    square = 4**2
    return f'4 squared is {square}'
