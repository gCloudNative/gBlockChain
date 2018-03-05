# -*- coding: utf-8 -*-

from flask.ext.sqlalchemy import SQLAlchemy

class NewSQLAlchemy(SQLAlchemy):
    def init_app(self, app):
        super(NewSQLAlchemy, self).init_app(app)
        from gBlockChain.models import *
        self.create_all()

extension = NewSQLAlchemy()
