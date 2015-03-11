# -*- coding: utf-8 -*-
"""Extensions module."""

from flask_oauthlib.client import OAuth

oauth = OAuth()

from flask.ext.assets import Environment

assets = Environment()

# Change this to HerokuConfig if using Heroku.
from flask.ext.appconfig import AppConfig

config = AppConfig()
