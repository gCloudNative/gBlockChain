#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint, request, abort, flash, redirect, url_for
from gBlockChain.utils import render_json, render_html, view, ValidationError, NotFoundError, Error
from multiprocessing.dummy import Pool as ThreadPool
from gBlockChain import config, app
from collections import defaultdict
import json
from gBlockChain.models import BlockChain, Host

from datetime import datetime, timedelta
from multiprocessing.dummy import Pool as ThreadPool


bp = Blueprint('chain', __name__, url_prefix='/api/v1/chain')
bp_html = Blueprint('chain_html', __name__, url_prefix='/chain')


@view(bp_html, '/', render_html('blockchain.html'), methods=['GET'])
def index():
    return dict(title=u"以太坊部署管理平台")

@view(bp_html, '/detail', render_html('blockchain_detail.html'), methods=['GET'])
def detail():
    return dict(title=u"以太坊部署管理平台")


@view(bp_html, '/create', render_html('blockchain_create.html'), methods=['GET', 'POST'])
def create(**kw):
    if request.method == 'POST':
        chain_name = kw.get('chain_name')
        chain_desc = kw.get('description')
        chain_owner = kw.get('owner')
        chain_developers = kw.get('developers')
        chain_testers = kw.get('testers')
        chain_opsers = kw.get('opsers')
        chain_type = kw.get('chain_type')
        chain_node_num = int(kw.get('chain_node_number'))

        print("链名称:", chain_name, "type:", type(chain_name))
        print("链描述:", chain_desc)
        print("链负责人:", chain_owner)
        print("链开发:", chain_developers)
        print("链测试:", chain_testers)
        print("链运维:", chain_opsers)
        print("链类型:", chain_type)
        print("节点数:", chain_node_num)


        chain = BlockChain.query.filter(BlockChain.name == chain_name).one_or_none()
        if not chain:
            BlockChain.create(name=chain_name, description=chain_desc,
                              owner=chain_owner, developers=chain_developers, testers=chain_testers, opsers=chain_opsers,
                              type=chain_type, nodes_init_num=chain_node_num)
            flash(u'添加链 {} 成功!'.format(chain_name))
        else:
            BlockChain.update(name=chain_name, description=chain_desc,
                              owner=chain_owner, developers=chain_developers, testers=chain_testers, opsers=chain_opsers,
                              type=chain_type, nodes_init_num=chain_node_num)
            flash(u'更新链 {} 成功!'.format(chain_name))



    return dict(title=u"区块链部署管理平台")



