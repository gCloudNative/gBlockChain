# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


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
