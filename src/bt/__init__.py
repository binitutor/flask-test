
from flask import Flask
from flask_oidc import OpenIDConnect
import os
# from okta import UsersClient
from okta.client import Client as UsersClient

app = None
oidc = None # OpenID Connect protocol
okta_client = None
uploads_dir = None

def create_app(bind=None):
    # declare variables as global, so that it can be used inside function
    global app
    global oidc
    global okta_client
    global uploads_dir

    app = Flask(__name__, static_folder='static')
    oidc = None
    app.app_context().push()
    # postgresdb.init_app(app)
    app.config["DEBUG"] = True

    '''
        declare the necessary configuration
    '''
    # app.config.from_object('config')
    # app.config["OIDC_CLIENT_SECRETS"] = 'client_secrets.json'
    # app.config["OIDC_COOKIE_SECURE"] = False
    # app.config["OIDC_CALLBACK_ROUTE"] = '/oidc/callback'
    # app.config["OIDC_SCOPES"] = ['openid', 'email', 'profile']
    # app.config["SECRET_KEY"] = 'abvkjsavdkjds'
    # app.config["OIDC_CLIENT_SECRETS"] = 'client_secrets.json'
    
    # try:
    #     oidc = OpenIDConnect(app)
    # except:
    #     app.config['OIDC_CLIENT_SECRETS'] = 'client_secrets.json'
    #     oidc = OpenIDConnect(app)
    # okta_client = UsersClient( 
    #         app.config['OKTA_DOMAIN'], 
    #         app.config['OKTA_API_KEY']
    #         )

    # # creating the upload directory
    # uploads_dir = os.path.join(app.instance_path, 'UPLOAD_FOLDER')
    # os.makedirs(uploads_dir, exists_ok=True)

    # from bt.runner import celery
    # celery.init_app(app)

    return app

create_app()