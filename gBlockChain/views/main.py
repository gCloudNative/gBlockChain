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


@view(bp_html, '/', None)
def index():
    return "Hello World!"
    
@view(bp_html, '/health', None)
def health():
    return 'OK'

@view(bp_html, '/status', None)
def status():
    return "200"
    

@view(bp, '/users', render_json, methods=['GET'])
def get_users():
    users = User.all()
    print(users)
    return { 'userTotal': len(users) }


