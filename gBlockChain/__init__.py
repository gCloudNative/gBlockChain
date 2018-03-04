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


from flask import Flask
app = Flask(__name__)
app.config.from_pyfile('config.py')


@app.route('/')
def index():
    return "Hello World!"

@app.route('/health')
def health():
    return "ok"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
