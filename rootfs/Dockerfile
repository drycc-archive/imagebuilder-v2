FROM minio/mc:RELEASE.2018-11-06T01-12-20Z as mc

FROM python:3.7-alpine

COPY . /
COPY --from=mc /usr/bin/mc /usr/bin/mc

ENV DOCKER_PY_VERSION 3.7.2

RUN apk add --update --virtual .dockerbuilder-rundeps \
    ca-certificates \
    bash \
  && pip3 install --disable-pip-version-check \
    --no-cache-dir \
    https://github.com/docker/docker-py/archive/$DOCKER_PY_VERSION.zip

CMD ["python3", "/deploy.py"]
