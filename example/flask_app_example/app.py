from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return 'This is a sample library that has been imported from local python repository'
