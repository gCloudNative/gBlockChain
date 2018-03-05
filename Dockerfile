#FROM python:2.7.14-alpine3.6
FROM python:3.6.4-alpine3.6

MAINTAINER Yang Sen <nuaays@gmail.com>

WORKDIR /

ENV TZ Asia/Shanghai
ENV APP_PORT 5000


RUN echo "https://mirror.tuna.tsinghua.edu.cn/alpine/v3.6/main/" > /etc/apk/repositories && \
    echo "https://mirror.tuna.tsinghua.edu.cn/alpine/v3.6/community/" >> /etc/apk/repositories

COPY ./requirements.txt /requirements.txt
#COPY ./pip.conf /etc/pip.conf

RUN apk --update add gcc libc-dev tzdata supervisor net-tools curl tree drill python3-dev py-mysqldb mariadb-dev build-base mariadb-client-libs && rm -rf /var/cache/apk/* 
RUN pip3 install -r /requirements.txt -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com
RUN ln -snf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && echo $TZ > /etc/timezone 

RUN mkdir /instance /data /logs

COPY ./gBlockChain /gBlockChain
COPY ./manage.py   /manage.py
COPY ./supervisord.conf /etc/supervisord.conf

VOLUME /logs
EXPOSE $APP_PORT

HEALTHCHECK --start-period=15s --interval=30s --timeout=20s --retries=3 CMD curl -s --fail http://localhost:$APP_PORT/health || exit 1

CMD ["supervisord", "-c", "/etc/supervisord.conf"]

