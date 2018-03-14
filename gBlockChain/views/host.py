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


bp = Blueprint('host', __name__, url_prefix='/api/v1/host')
bp_html = Blueprint('host_html', __name__, url_prefix='/host')


@view(bp_html, '/', render_html('host_create.html'), methods=['GET', 'POST'])
def create(**kw):
    if request.method == 'POST':
        host_ip = kw.get('host_ip')
        docker_port = kw.get('docker_port')
        cadvisor_port = kw.get('cadvisor_port')
        description = kw.get('description')
        host_os = kw.get('host_os')
        host_label = kw.get('host_label')

        print("主机IP:", host_ip)
        print("Docker端口:", docker_port)
        print("cAdvisor端口:", cadvisor_port)
        print("描述:", description)
        print("主机OS:", host_os)
        print("主机标签:", host_label)


        host_ip = kw.get('host_ip')
        docker_port = kw.get('docker_port')
        cadvisor_port = kw.get('cadvisor_port')
        description = kw.get('description')
        host_os = kw.get('host_os')
        host_label = kw.get('host_label')

        host = Host.query.filter(Host.ip == host_ip).one_or_none()
        if not host:
            Host.create(ip=host_ip, description=description,
                        docker_api_port=docker_port, cadvisor_api_port=cadvisor_port,
                        cloud_ostype=host_os, host_label=host_label)
            flash(u'添加主机 {} 成功!'.format(host_ip))
        else:
            Host.update(ip=host_ip, description=description,
                        docker_api_port=docker_port, cadvisor_api_port=cadvisor_port,
                        cloud_ostype=host_os, host_label=host_label)
            flash(u'更新主机 {} 成功!'.format(host_ip))


    return dict(title=u"以太坊部署管理平台")
