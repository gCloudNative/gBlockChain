


## deploy ethereum chain using docker
```

第一个节点在10.12.0.145
docker run --rm --net=host ethereum/client-go:stable --datadir datadir/ --rpc --rpcapi eth,admin,personal,miner,txpool,net --maxpeers 25 --networkid 19512 --port 37001 --rpcport 7001 --rpcaddr 0.0.0.0

enode://5e979b6cb62ffc5cfd0e69d0abca0de32a197d3431f9670ad75c1f8b9c9042abdcc7b14e79065aca7f2ac4ac0d5644c21411223ddfcc16a94208cab2fb3d5aed@[::]:37001

第二个节点
docker run --rm --net=host ethereum/client-go:stable --datadir datadir/ --rpc --rpcapi eth,admin,personal,miner,txpool,net --maxpeers 25 --networkid 19512 --port 37002 --rpcport 7002 --rpcaddr 0.0.0.0 --bootnodes enode://5e979b6cb62ffc5cfd0e69d0abca0de32a197d3431f9670ad75c1f8b9c9042abdcc7b14e79065aca7f2ac4ac0d5644c21411223ddfcc16a94208cab2fb3d5aed@10.12.0.145:37001

第三个节点
docker run --rm --net=host ethereum/client-go:stable --datadir datadir/ --rpc --rpcapi eth,admin,personal,miner,txpool,net --maxpeers 25 --networkid 19512 --port 37003 --rpcport 7003 --rpcaddr 0.0.0.0 --bootnodes enode://5e979b6cb62ffc5cfd0e69d0abca0de32a197d3431f9670ad75c1f8b9c9042abdcc7b14e79065aca7f2ac4ac0d5644c21411223ddfcc16a94208cab2fb3d5aed@10.12.0.145:37001

第四个节点
docker run --rm --net=host ethereum/client-go:stable --datadir datadir/ --rpc --rpcapi eth,admin,personal,miner,txpool,net --maxpeers 25 --networkid 19512 --port 37004 --rpcport 7004 --rpcaddr 0.0.0.0 --bootnodes enode://5e979b6cb62ffc5cfd0e69d0abca0de32a197d3431f9670ad75c1f8b9c9042abdcc7b14e79065aca7f2ac4ac0d5644c21411223ddfcc16a94208cab2fb3d5aed@10.12.0.145:37001


创建账号
curl -X POST -H "Content-type: application/json" --data '{"jsonrpc":"2.0","method":"personal_newAccount", "params":["geerong"],"id":67}' 10.12.0.145:7001

查询账号
curl -X POST -H "Content-type: application/json" --data '{"jsonrpc":"2.0","method":"eth_accounts", "params":[],"id":67}' 10.12.0.145:7001

curl -X POST -H "Content-type: application/json" --data '{"jsonrpc":"2.0","method":"eth_coinbase", "params":[],"id":67}' 10.12.0.145:7001


查询账号余额
curl -X POST -H "Content-type: application/json" --data '{"jsonrpc":"2.0","method":"eth_getBalance", "params":["0xbab010d005eac1c0a1148283dd438c287d864bfe","latest"], "id":67}' 10.12.0.145:7001





查询连接节点及个数

curl -X POST -H "Content-type: application/json" --data '{"jsonrpc":"2.0","method":"admin_peers","params":[],"id":67}' 10.12.0.145:7001 | python -m json.tool

curl -X POST -H "Content-type: application/json" --data '{"jsonrpc":"2.0","method":"net_peerCount","params":[],"id":67}' 10.12.0.145:7001 | python -m json.tool

查询区块个数
curl -X POST -H "Content-type: application/json" --data '{"jsonrpc":"2.0","method":"eth_blockNumber", "params":[],"id":67}' 10.12.0.145:7001


开始挖矿
curl -X POST -H "Content-type: application/json" --data '{"jsonrpc":"2.0","method":"miner_start", "params":[],"id":67}' 10.12.0.145:7001

停止挖矿
curl -X POST -H "Content-type: application/json" --data '{"jsonrpc":"2.0","method":"miner_stop", "params":[],"id":67}' 10.12.0.145:7001



查询版本
curl -X POST -H "Content-type: application/json" --data '{"jsonrpc":"2.0","method":"net_version", "params":[],"id":67}' 10.12.0.145:7001
```

