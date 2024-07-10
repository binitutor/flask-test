
from bt import app
from absl import flags

# if not flags.FLAGS.is_parsed():
#     flags.FLAGS(['', '--heroku', '--test_email', '--bt_mock'])

# @app.before_request
# def verify_user_cred():
#     pass

# @app.route('file_upload', method=['PUT'])
# def upload():
#     pass

# @app.route('/async_job/<string:uuid_text>')
# def async_job(uuid_text):
#     pass

@app.route('/')
def index():
    pass

# @app.route('/login')
# def login():
#     pass

# @app.route('/logout')
# def logout():
#     pass

# on terminal: python src\api.py
if __name__=='__main__':
    print('(__main__) BiniTutor File Processor API is running...')
    app.run(debug=True)