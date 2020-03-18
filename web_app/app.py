from flask import Flask
webapp = Flask(__name__)


@webapp.route('/')
def hello():
    return "Hello World!"

def start():
    webapp.run()
