from datetime import datetime
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome'
@app.route('/greet')
def greet():
    time = datetime.now().hour
    if time >= 0 and time < 12:
        return 'Good Morning!'
    elif time >= 12 and time < 16:
        return 'Good Afternoon!'
    else:
        return 'Good Evening!'