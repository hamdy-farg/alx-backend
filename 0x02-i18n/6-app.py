#!/usr/bin/env python3
"""
A Basic flask application
"""
from typing import Dict, Union
from flask import Flask, render_template, request, g
from flask_babel import Babel, _

class Config(object):
    """
    Application configuration class
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)

def get_locale() -> str:
    """
    Gets locale from request object
    """
    options = [
        request.args('local','').strip(),
        g.user.get('locale',None) if g.user else None,
        request.accept_languages.best_match(app.config['LANGUAGES']),
        Config.BABEL_DEFAULT_LOCALE
    ]
    for locale in options:
        if locale and locale in  Config.LANGUAGES:
            return locale
babel.init_app(app, locale_selector=get_locale)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

def get_user(id) -> Union[Dict[str, Union[str, None]], None]:
    """
    Validate user login details
    Args:
        id (str): user id
    Returns:
        (Dict): user dictionary if id is valid else None
    """
    return users.get(int(id))

@app.before_request
def before_request():
    """
    Adds valid user to the global session object `g`
    """
    g.user = get_user(request.args.get('login_as', 0))

@app.route('/name', strict_slashes=False)
def index() -> str:
    """
    Render basic html template
    """
    return render_template('6-index.html',
    hello_world=_('Hello_world'),
    loged_in_as =_('loged_in_as'), username=g.user,
    not_loged_in=_('not_loged_in'))

if __name__ == '__main__':
    app.run()