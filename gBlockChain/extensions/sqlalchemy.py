# -*- coding: utf-8 -*-

from flask_sqlalchemy import SQLAlchemy

class NewSQLAlchemy(SQLAlchemy):
    def init_app(self, app, use_native_unicode='utf8' ):
        super(NewSQLAlchemy, self).init_app(app)
        self.create_all()


extension = NewSQLAlchemy()

