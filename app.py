from flask import Flask


app = Flask(__name__)

app.config['SECRET_KEY'] = 'try-to-guess'

from routes import *

if __name__ == '__main__':
    app.run()
