#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gBlockChain.lib.database import db, Model, Column, relationship, reference_col


class BlockChain(Model):
    __tablename__ = 'chain'

    id = Column(db.Integer, primary_key=True, autoincrement=True, unique=True, index=True)
    name = Column(db.String(64), unique=True, nullable=False)

    type = Column(db.String(64), default="ethereum")
    image = Column(db.String(64), default="ethereum/client-go:stable")

    network_id = Column(db.Integer, default=19512)
    nodes_init_num = Column(db.Integer, default=1)
    boot_node = Column(db.String(64), default="")

    owner = Column(db.String(64), default="")
    developers = Column(db.String(64), default="")
    testers = Column(db.String(64), default="")
    opsers = Column(db.String(64), default="")

    # uuid = Column(String(64), nullable=False, unique=True, index=True)
    description = Column(db.Text, default="")

