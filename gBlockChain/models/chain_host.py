#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gBlockChain.lib.database import db, Model, Column, relationship, reference_col


class Host(Model):
    __tablename__ = 'host'
    id = Column(db.Integer, primary_key=True, autoincrement=True, unique=True)
    ip = Column(db.String(64), nullable=False, index=True, unique=True)

    cpu_core_num = Column(db.Integer, default=1)
    mem_total_size = Column(db.Integer, default=8)
    disk_total_size = Column(db.Integer, default=40)
    band_width = Column(db.Integer, default=1)

    container_limit = Column(db.Integer, default=20)
    docker_api_port = Column(db.Integer, default=2375)
    cadvisor_api_port = Column(db.Integer, default=4033)

    description = Column(db.Text, default="")
    host_label = Column(db.String(32), default="")

    cloud_ostype = Column(db.String(32), default="CentOS")
    cloud_vendor = Column(db.String(32), default="")
    cloud_region = Column(db.String(32), default="")
