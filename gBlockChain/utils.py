# -*- coding: utf-8 -*-

from functools import wraps
from flask import request, render_template, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.wrappers import Response
from werkzeug import BaseResponse
import json, re, datetime, time, socket, itertools, requests


def list_models(db):
    classes, models, table_names = [], [], []
    for clazz in db.Model._decl_class_registry.values():
        try:
            table_names.append(clazz.__tablename__)
            classes.append(clazz)
        except:
            pass

    for table in db.metadata.tables.items():
        if table[0] in table_names:
            models.append(classes[table_names.index(table[0])])

    return models

def load_module_dynamic(module):
    def _deco(f):
        @wraps(f)
        def __deco(*args, **kwargs):
            for name in getattr(module, 'module_priority_chain', []):
                module_name = '{0}.{1}'.format(module.__name__, name)

                try:
                    _module = __import__(module_name, fromlist=[''])
                except ImportError:
                    continue

                kwargs.update(dict(module=_module))
                f(*args, **kwargs)

            # load module based on filename
            import pkgutil
            for _loader, name, _ispkg in pkgutil.iter_modules(module.__path__):
                module_name = '{0}.{1}'.format(module.__name__, name)
                # 'app_name.extensions.xxx' ==> 'xxx', and check blacklist
                if module_name.split('.')[-1] in getattr(module, 'module_blacklist', []) + getattr(module, 'module_priority_chain', []):
                    continue

                _module = __import__(module_name, fromlist=[''])

                kwargs.update(dict(module=_module))
                f(*args, **kwargs)

        return __deco
    return _deco


def render_json(result):
    json_result = json.dumps(result, default=json_default_format)
    print(json_result)
    return Response(json_result,  mimetype='application/json')


def render_html(template, **defaults):
    def wrapped(result):
        variables = defaults.copy()
        # data = json.loads( json.dumps(result, default=json_default_format)  )
        variables.update(result)
        return render_template(template, **variables)
    return wrapped


def view(instance, url, renderer=None, *args, **kwargs):
    super_route = instance.route

    defaults = kwargs.pop('defaults', {})
    route_id = object()
    defaults['_route_id'] = route_id

    def deco(f):
        @super_route(url, defaults=defaults, *args, **kwargs)
        @wraps(f)
        def decorated_function(*args, **kwargs):
            this_route = kwargs.get('_route_id')
            if not getattr(f, 'is_route', False):
                del kwargs['_route_id']

            # pass post data to kwargs.
            if request.method in ['POST', 'PUT']:
                try:
                    _params = json.loads(request.data)
                    #print( "_params", _params )
                except ValueError as e:
                    # _form = request.form
                    # _params = {k: _form[k] for k in _form}
                    _params = None
                    # raise ValidationError(e)

                if isinstance(_params, dict):
                    kwargs.update(_params)

            result = f(*args, **kwargs)

            if this_route is not route_id:
                return result

            # catch redirects.
            if isinstance(result, (Response, BaseResponse)):
                return result

            if renderer is None:
                return result
            return renderer({'data': result})

        decorated_function.is_route = True
        return decorated_function

    return deco


def json_default_format(o):
    if type(o) is datetime.date or type(o) is datetime.datetime:
        return o.isoformat()

    if hasattr(o, 'to_dict'):
        return o.to_dict()


class Error(Exception):
    def __init__(self, msg, code=500):
        self.msg = msg
        self.code = code
        Exception.__init__(self, self.msg)

    def to_dict(self):
        return dict(msg=self.msg, code=self.code)


class NotFoundError(Error):
    def __init__(self, obj, id):
        self.msg = '{} {} Not found'.format(obj, id)
        Error.__init__(self, self.msg, 404)


class ValidationError(Error):
    def __init__(self, msg='', data=None):
        self.msg = 'Validation error: %s' % msg
        Error.__init__(self, data or self.msg)


class CallError(Error):
    def __init__(self, msg, url=''):
        self.msg = 'Call %s error: %s' % (url, msg)
        Error.__init__(self, self.msg)


class PermissionError(Error):
    def __init__(self, msg):
        self.msg = 'Permission denied: %s' % msg
        Error.__init__(self, self.msg, 403)


class JSONRPCClient(object):
    def __init__(self, server):
        self.url = 'http://{}'.format(server)
        self.data = {
            'id': 1,
            'jsonrpc': '2.0',
            'method': '',
            'params': []}

    def call(self, method, params=None):
        if params is None:
            params = []

        try:
            r = requests.post(self.url, json=dict(self.data, method=method, params=params), timeout=3)
        except Exception as e:
            raise CallError(str(e), url=self.url)

        resp = r.json()

        if 'error' in resp:
            raise CallError(resp['error'], url=self.url)
        else:
            return resp['result']


def current_username():
    try:
        username = session.get('CAS_USERNAME', {}).get('username')
    except RuntimeError:
        username = ""

    return username
    

def lazyproperty(fn):
    attr_name = '_lazy_' + fn.__name__
    @property
    def _lazyprop(self):
        if not hasattr(self, attr_name):
            setattr(self, attr_name, fn(self))
        return getattr(self, attr_name)
    return _lazyprop

