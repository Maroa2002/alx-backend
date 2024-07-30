#!/usr/bin/env python3
""" Flask app """
from flask import Flask, render_template, request
from flask_babel import Babel, _

app = Flask(__name__)  # Flask app


class Config:
    """ configuration class """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


# load the cofiguration from the Config class
app.config.from_object(Config)

babel = Babel(app)  # Babel object


@babel.localeselector
def get_locale():
    """ retrieves the locale """
    # gets locale from request
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/")
def index():
    """ home route """
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run(debug=True)
