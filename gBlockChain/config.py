# -*- coding: utf-8 -*-
import os

basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = os.environ.get('DEBUG') or True
SECRET_KEY = os.environ.get('SECRET_KEY') or ')=+A54#:aA5TFFND5W\t}!"W~E(k07*P'


APP_NAME = 'gBlockChain'
APP_LOG = '/tmp/{}.log'.format(APP_NAME)


# SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '../data/app.db')
# SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@mysql:3306/blockchain?charset=utf8'
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@127.0.0.1:13306/blockchain?charset=utf8'
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




# APP BRAND SETTING FOR WEB
APP_BRAND=u'区块链部署管理平台'
APP_BRAND_ALT=u'区块链云平台'
APP_AUTHOR=u'平台框架组'
APP_AUTHOR_EMAIL=["nuaays@gmail.com"]
APP_INTRO_CONTENT=u"基于以太坊的区块链一键部署管理平台"

# WEB
ASSETS_DEBUG=False
WEB_LAYOUT_TOPBAR_FIXED=False
WEB_STATIC_COMPRESSED=True
WEB_SECONDBAR_ENABLED=False
WEB_SIDERBAR_TOGGLE_ELSE_HIDE=False #True: sidebar-main-toggle , False: sidebar-main-hide
WEB_SIDERBAR_COLLAPSABLED=False
WEB_SIDERBAR_USERINFO_SHOW=False

