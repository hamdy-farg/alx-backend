#!/usr/bin/env python3
"""
A Basic flask application
"""
from flask import Flask, g
from flask import request
from flask import render_template
from flask_babel import Babel

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

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

def get_user()-> dict:
    """
    Get User from db
    """
    user_id = request.args.get("login_as")

    if user_id and user_id.isdigit():
        return users.get(int(user_id))
 
    return None

@app.before_request
def before_request():
    """
    Executed before all other functions to check if a user is logged in.
    Sets the user on flask.g if found.
    """
    g.user = get_user()


def get_locale() -> str:
    """
    Gets locale from request object
    """
     # 1. Check for locale in URL parameters
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale

    # 2. Check if the user is logged in and return their preferred locale
    if g.user and g.user.get('preferred_locale') in app.config['LANGUAGES']:
        return g.user['preferred_locale']

    # 3. Fallback to the best match from request headers
    return request.accept_languages.best_match(app.config['LANGUAGES']) or app.config['BABEL_DEFAULT_LOCALE']

babel.init_app(app, locale_selector=get_locale)

@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Renders a basic html template
    """
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run()