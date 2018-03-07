# -*- coding: utf-8 -*-

from flask import Blueprint, request, abort, flash, redirect, url_for
from gBlockChain.utils import render_json, render_html, view, ValidationError, NotFoundError, Error
from multiprocessing.dummy import Pool as ThreadPool
from gBlockChain import config, app
from collections import defaultdict
import json
from gBlockChain.models import User


bp = Blueprint('main', __name__, url_prefix='/api/v1')
bp_html = Blueprint('main_html', __name__, url_prefix='')


@view(bp_html, '/', render_html('index.html'), methods=['GET'])
def index():
    return dict(title=u"区块链部署管理平台" )

@view(bp_html, '/test', render_html('index_blank.html'), methods=['GET'])
def test():
    return dict(title=u"区块链部署管理平台" )
    
@view(bp_html, '/health', None)
def health():
    return 'OK'

@view(bp_html, '/status', None)
def status():
    return "200"
    

@view(bp_html, '/users', None, methods=['GET'])
def get_users():
    users = User.all()
    print(users)
    return ""

@view(bp, '/users', render_json, methods=['GET'])
def get_users():
    users = User.all()
    print(users)
    return {}



