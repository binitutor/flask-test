
from bt import app

@app.route('/')
def index():
    print('called index route...')
    return 'called index route...'

# on terminal: python src\api.py
if __name__=='__main__':
    print('(__main__) BiniTutor File Processor API is running...')
    app.run(debug=True)