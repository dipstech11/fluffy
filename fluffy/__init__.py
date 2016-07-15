import logging
import sys

from flask import Flask


app = Flask(__name__)
app.config.from_envvar('FLUFFY_SETTINGS')
app.logger.addHandler(logging.StreamHandler(sys.stderr))
app.logger.setLevel(logging.DEBUG)


@app.context_processor
def home_url():
    return {'home_url': app.config['HOME_URL']}
