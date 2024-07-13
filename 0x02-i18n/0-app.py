#!/usr/bin/env python3
"""
A Basic flask appliction
"""
from flask import render_template, request, Flask
app = Flask(__name__)

@app.route('/')
def welcome_page() -> str:
    """ 
    Render a basic html template
    """
    return render_template('0-index.html')

if __name__ == '__main__':
    app.run()