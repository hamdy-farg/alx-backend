#!/usr/bin/env python3
"""
A Basic flask appliction
"""
from flask import Flask
from flask import render_template
from flask_babel import Babel
from flask import request

class Config(object):
    """
    Application configuration class
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCAL = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


# 
app = Flask(__name__)
app.config.from_object(Config)

#
babel = Babel(app)


@app.route('/', strict_slashes=False)
def index() -> str:
    """ 
    Render basic html template
    """
    return render_template('1-index.html')

if __name__ == '__main__':
    app.run()