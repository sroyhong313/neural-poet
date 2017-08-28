# app/__init__.py

# third-party imports
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import pymongo
from jinja2 import evalcontextfilter, Markup, escape
import re
# local imports
from config import app_config

# mongodb variable initialization
client = pymongo.MongoClient("localhost", 27017)
mongodb = client["neuralpoet"]
poem_col = mongodb["poems"]
poem_col.create_index([("textfield", "text")])

_paragraph_re = re.compile(r'(?:\r\n|\r|\n){2,}')


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')

    Bootstrap(app)

    @app.template_filter()
    @evalcontextfilter
    def nl2br(eval_ctx, value):
        result = u'\n\n'.join(u'<p>%s</p>' % p.replace('\n', '<br>\n') \
            for p in _paragraph_re.split(escape(value)))
        if eval_ctx.autoescape:
            result = Markup(result)
        return result

    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)

    @app.errorhandler(403)
    def forbidden(error):
        return render_template('errors/403.html', title='Forbidden'), 403

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('errors/404.html', title='Page Not Found'), 404

    @app.errorhandler(500)
    def internal_server_error(error):
        return render_template('errors/500.html', title='Internal Server Error'), 500

    return app

