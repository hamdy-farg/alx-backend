#!/usr/bin/env python3
"""
A Basic flask application
"""
from flask import Flask
from flask import request
from flask import render_template
from flask_babel import Babel


class Config(object):
    """
    Application configuration class
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


# Instantiate the application object
app = Flask(__name__)
app.config.from_object(Config)

# Wrap the application with Babel
babel = Babel(app)


def get_locale() -> str:
    """
    Gets locale from request object
    """
    locale = request.args.get('locale')
    print(locale)
    if locale in app.config['LANGUAGES']:
        return locale
    
    return  request.accept_languages.best_match(app.config['LANGUAGES'])

babel.init_app(app, locale_selector=get_locale)

@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Renders a basic html template
    """
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run()