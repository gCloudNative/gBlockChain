# -*- coding: utf-8 -*-
import os

basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = os.environ.get('DEBUG') or True
SECRET_KEY = os.environ.get('SECRET_KEY') or ')=+A54#:aA5TFFND5W\t}!"W~E(k07*P'


APP_NAME = 'gBlockChain'
APP_LOG = '/tmp/{}.log'.format(APP_NAME)


#SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '../data/app.db')
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@mysql:3306/blockchain?charset=utf8'
# SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@127.0.0.1:13306/blockchain?charset=utf8'
SQLALCHEMY_COMMIT_ON_TEARDOWN=True
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = False




# FLASK Redis
REDIS_HOST='redis'
REDIS_PORT=6379
REDIS_DB='0'
REDIS_PASSWORD=''


# FLASK Cache
CACHE_REDIS_HOST=REDIS_HOST #'redis'
CACHE_REDIS_PORT=REDIS_PORT
CACHE_REDIS_DB='1'
CACHE_REDIS_PASSWORD=''
