FROM docker.io/minio/mc:latest as mc


FROM gcr.io/kaniko-project/executor:v1.3.0 as kaniko


FROM docker.io/library/python:3.9-alpine

COPY . /
COPY --from=mc /usr/bin/mc /bin/mc
COPY --from=kaniko /kaniko /kaniko

RUN echo "http://dl-cdn.alpinelinux.org/alpine/edge/community" >> /etc/apk/repositories \
  && apk add --update --virtual .imagebuilder-rundeps \
    caddy \
    ca-certificates \
    bash \
  && pip3 install --disable-pip-version-check \
    --no-cache-dir \
    requests==2.24.0

CMD ["python3", "/deploy.py"]
