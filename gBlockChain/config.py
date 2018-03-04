# -*- coding: utf-8 -*-
import os

basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG=os.environ.get('DEBUG') or False
SECRET_KEY = os.environ.get('SECRET_KEY') or ')=+A54#:aA5TFFND5W\t}!"W~E(k07*P'


APP_NAME = 'gBlockChain'
APP_LOG = '/tmp/gBlockChain.log'



