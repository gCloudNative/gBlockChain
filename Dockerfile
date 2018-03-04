FROM python:2.7.14-alpine3.6

MAINTAINER Yang Sen <nuaays@gmail.com>

WORKDIR /

ENV TZ Asia/Shanghai
ENV APP_PORT 5000


RUN echo "https://mirror.tuna.tsinghua.edu.cn/alpine/v3.6/main/" > /etc/apk/repositories && \
    echo "https://mirror.tuna.tsinghua.edu.cn/alpine/v3.6/community/" >> /etc/apk/repositories

COPY ./requirements.txt /requirements.txt


RUN apk update && apk add tzdata supervisor net-tools curl tree drill && \
    ln -snf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && echo $TZ > /etc/timezone && \
    pip install -r /requirements.txt  -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com && \
    rm -rf /var/cache/apk/* 

RUN mkdir /instance /data /logs

COPY ./gBlockChain /gBlockChain
COPY ./supervisord.conf /etc/supervisord.conf

VOLUME /logs
EXPOSE $APP_PORT

HEALTHCHECK --start-period=15s --interval=30s --timeout=20s --retries=3 CMD curl --fail http://localhost:$APP_PORT/health || exit 1

CMD ["supervisord", "-c", "/etc/supervisord.conf"]

