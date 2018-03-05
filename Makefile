VIRTUALENV_DIR := .venv

help:
	@echo "  dev         launch Debug Environment"
	@echo "  server      launch Web Server"
	@echo "  install     same to pip"
	@echo "  shell       open context shell"
	@echo "  pip         pip install packages"
	@echo "  url         list all urls"
	@echo "  clean       clean .pyc files"
	@echo "  db          init / upgrade db operation"

i install: pip

pip:
	pip install virtualenv
	virtualenv --python=/usr/local/bin/python3 $(VIRTUALENV_DIR)
	$(VIRTUALENV_DIR)/bin/pip3 install -r requirements.txt -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com

dev:
	$(VIRTUALENV_DIR)/bin/python3 manage.py dev

s server:
	$(VIRTUALENV_DIR)/bin/python3 manage.py server

g:
	$(VIRTUALENV_DIR)/bin/gunicorn --name=gBlockChain --reload --reload-engine=poll --workers=4 --worker-class=gevent --bind=0.0.0.0:5000 --log-level=DEBUG --access-logfile=access.log --error-logfile=error.log gBlockChain:app

t:
	$(VIRTUALENV_DIR)/bin/gunicorn --name=gBlockChain --preload --workers=4 --worker-class=tornado --bind=0.0.0.0:5000 --log-level=DEBUG --access-logfile=access.log --error-logfile=error.log gBlockChain:app

u:
	$(VIRTUALENV_DIR)/bin/uwsgi --socket /tmp/uwsgi.sock --gevent 100 --http 127.0.0.1:5000 --module titans --callable app

shell:
	$(VIRTUALENV_DIR)/bin/pip3 install ipython
	$(VIRTUALENV_DIR)/bin/python3 manage.py shell

url:
	$(VIRTUALENV_DIR)/bin/python3 manage.py url

clean:
	$(VIRTUALENV_DIR)/bin/python3 manage.py clean

db:
	$(VIRTUALENV_DIR)/bin/python3 manage.py db $(ARG)

build:
	docker build -t gBlockChain:0.0.1 .

