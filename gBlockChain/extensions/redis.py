# -*- coding: utf-8 -*-

# from flask_redis import Redis
from flask_cache import Cache
from gBlockChain import config

class NewCache(Cache):
    def init_app(self, app):
        config_cache = {
        'CACHE_TYPE': 'redis',
        'CACHE_REDIS_HOST': config.CACHE_REDIS_HOST,
        'CACHE_REDIS_PORT': config.CACHE_REDIS_PORT,
        'CACHE_REDIS_DB': config.CACHE_REDIS_DB,
        'CACHE_REDIS_PASSWORD': config.CACHE_REDIS_PASSWORD
        }
        super(NewCache, self).init_app(app, config_cache)

extension = NewCache()
