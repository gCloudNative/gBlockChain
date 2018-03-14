#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gBlockChain.lib.database import db, Model, Column, relationship, reference_col
from gBlockChain.utils import JSONRPCClient, lazyproperty
import traceback
from gBlockChain import config, app


class Node(Model):
    __tablename__ = 'eth_node'

    ip = Column(db.String(64), nullable=False)
    p2p_port = Column(db.Integer, nullable=False)
    rpc_port = Column(db.Integer, nullable=False)
    rpc_mod = Column(db.String(256), nullable=False)
    boot_nodes = Column(db.String(256), nullable=True)
    enable_mine = Column(db.Boolean, default=False)
    mine_thread = Column(db.Integer, default=1)
    etherbase = Column(db.String(256))
    per_cpu_speed = Column(db.Float, nullable=False)
    version = Column(db.String(32), nullable=False)
    memory = Column(db.Integer, nullable=False)
    container_name = Column(db.String(256))
    chain_id = Column(db.Integer, nullable=False)


    def deploy(self, ip_hostname_map):
        cmd = '--datadir datadir/ --port {} --rpcaddr=0.0.0.0 --rpcport {} --rpc --rpcapi {} {} {} {} --nodiscover --nousb --syncmode=fast --ipcpath /root/eth.ipc'.format(
            self.p2p_port,
            self.rpc_port,
            self.rpc_mod,
            self.enable_mine and '--mine --minerthreads {}'.format(self.mine_thread or 1) or '',
            self.enable_mine and '--etherbase {}'.format(self.etherbase) or '',
            self.boot_nodes and '--bootnodes {}'.format(self.boot_nodes) or '',
        )

        app.logger.info('Cmd: {}'.format(cmd))

        try:
            s = Service.new_bc_service(self.version, self.memory, ip_hostname_map[self.ip], cmd=cmd.split())
            result = s.start()
            self.container_name = result['Containers'][0]
        except Exception, e:
            # app.logger.error('Failed to start node {} (rpc_port: {}): {}'.format(self.ip, self.rpc_port, str(e)))
            return e

        return self

    @lazyproperty
    def rpc(self):
        return JSONRPCClient('{}:{}'.format(self.ip, self.rpc_port))

    @lazyproperty
    def has_admin_mod(self):
        return 'admin' in self.rpc_mod.split(',')

    @lazyproperty
    def eth_blockNumber(self):
        return int(self.rpc.call('eth_blockNumber'), 16)

    @lazyproperty
    def admin_nodeInfo(self):
        return self.rpc.call('admin_nodeInfo')

    @lazyproperty
    def admin_peers(self):
        return self.rpc.call('admin_peers')

    @lazyproperty
    def eth_coinbase(self):
        return self.rpc.call('eth_coinbase')

    @lazyproperty
    def eth_accounts(self):
        return self.rpc.call('eth_accounts')

    @lazyproperty
    def eth_protocolVersion(self):
        return self.rpc.call('eth_protocolVersion')

    @lazyproperty
    def eth_gasPrice(self):
        return self.rpc.call('eth_gasPrice')

    def miner_start(self):
        return self.rpc.call('miner_start')

    def miner_stop(self):
        return self.rpc.call('miner_stop')

