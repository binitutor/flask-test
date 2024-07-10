
from flask import Flask

app = None

def create_app(bind=None):
    # declare variables as global, so that it can be used inside function
    global app
    app = Flask(__name__, static_folder='static')
    app.app_context().push()
    app.config["DEBUG"] = True

    return app

create_app()