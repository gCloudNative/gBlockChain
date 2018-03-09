# -*- coding: utf-8 -*-
import sys
if sys.version_info[0] == 2:
    reload(sys)
    sys.setdefaultencoding("utf-8")
if sys.version_info[0] == 3:
    if sys.version_info[1] <= 3:
        import imp
        imp.reload(sys)
    else:
        import importlib
        importlib.reload(sys)

from flask import Flask, render_template, request, flash, redirect, session, current_app, g
from gBlockChain.utils import load_module_dynamic, json_default_format, Error, render_json, PermissionError
from gBlockChain import extensions, views
from gBlockChain.models import *
import json, datetime, pprint


from flask import Flask
app = Flask(__name__, static_folder='static', static_url_path='/static', template_folder='templates', instance_relative_config=False)
app.config.from_pyfile('config.py')



@load_module_dynamic(extensions)
def register_extensions(app, **kw):
    if hasattr(kw['module'], 'extension'):
        getattr(kw['module'].extension, 'init_app')(app)
        app.logger.debug('loading extension: %s => register' % kw['module'].__name__)
        try:
            kw['module'].extension.create_all()
        except Exception as e:
            pass
    else:
        app.logger.debug('loading extension: %s => ignore' % kw['module'].__name__)


@load_module_dynamic(views)
def register_blueprints(app, **kw):
    for i in ['bp', 'bp_html']:
        if hasattr(kw['module'], i):
            app.register_blueprint(getattr(kw['module'], i))
            app.logger.debug('loading blueprint: %s => register' % kw['module'].__name__)
        else:
            app.logger.debug('loading blueprint: %s => ignore' % kw['module'].__name__)


def register_errorhandlers(app):
    def render_error_html(error):
        error_code = getattr(error, 'code', 500)
        return render_template('error/{0}.html'.format(error_code)), error_code

    for errcode in [401, 404, 500]:
        app.errorhandler(errcode)(render_error_html)

    def render_error(error):
        if request.path.startswith('/api/'):
            e = error.to_dict()
            return render_json(e)
        else:
            flash(str(error), 'error')
            return redirect(request.referrer)

    for err in [Error]:
        app.errorhandler(err)(render_error)


def register_template_filters(app):
    @app.template_filter('json')
    def to_pretty_json(data, indent=2):
        if isinstance(data, basestring):
            return data
        return json.dumps(data, indent=indent, ensure_ascii=False, default=json_default_format)

    @app.template_filter('datetime')
    def format_timestamp(data, fmt='%Y-%m-%d %H:%M:%S'):
        if isinstance(data, datetime.datetime):
            return data.strftime(fmt)
        else:
            return datetime.fromtimestamp(data).strftime(fmt)

def register_loggers(app):
    import logging
    from logging.handlers import SMTPHandler

    stream_handler = logging.StreamHandler()
    file_handler = logging.FileHandler(app.config['APP_LOG'])
    # mail_handler = SMTPHandler('', 'gBlockChain', app.config['ADMINS_EMAIL'], 'gBlockChain failed!')

    formatter = logging.Formatter(
        '%(asctime)s\t%(levelname)s\t%(message)s '
        '[in %(pathname)s:%(lineno)d]'
    )

    stream_handler.setLevel(logging.DEBUG)
    file_handler.setLevel(logging.DEBUG)
    # mail_handler.setLevel(logging.ERROR)

    stream_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)
    # mail_handler.setFormatter(formatter)

    app.logger.addHandler(stream_handler)
    app.logger.addHandler(file_handler)
    #app.logger.addHandler(mail_handler)

    if not app.config.get('DEBUG'):
        app.logger.setLevel(logging.INFO)


with app.app_context():
    register_extensions(app)
    register_blueprints(app)
    register_errorhandlers(app)
    register_loggers(app)
    register_template_filters(app)
    if config.DEBUG:
        pprint.pprint(current_app.extensions)

    # app.redis = current_app.extensions['redis']
    # app.sqlalchemy = current_app.extensions['sqlalchemy']
    # app.sqlalchemy.create_all()

    #from gBlockChain.models import *
    # pprint.pprint( app.sqlalchemy )
    # app.sqlalchemy.create_all()




