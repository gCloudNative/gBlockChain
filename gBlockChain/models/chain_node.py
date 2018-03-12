#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gBlockChain.lib.database import db, Model, Column, relationship, reference_col


class ChainNode(Model):
    __tablename__ = 'chain_node'

    chain_id = Column(db.String, nullable=False, unique=True, index=True)
    chain_name = Column(db.String, nullable=False)
    chain_type = Column(db.String, default="secondary")
    chain_image = Column(db.String, default="")
