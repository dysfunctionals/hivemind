from flask import Flask

from hivemind.config import config

app = Flask(__name__)

app.config.update(config)

if 'VIEW_CONFIG' in app.config:
    # Allow view config access in templates
    app.jinja_env.globals['VIEW_CONFIG'] = app.config['VIEW_CONFIG']
else:
    app.jinja_env.globals['VIEW_CONFIG'] = {}

app.secret_key = app.config["SESSION_KEY"]

from hivemind import views  # noqa F401, E402
