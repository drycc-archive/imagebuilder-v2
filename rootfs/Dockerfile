FROM minio/mc:latest as mc


FROM gcr.io/kaniko-project/executor:v0.24.0 as kaniko


FROM python:3.8-alpine

COPY . /
COPY --from=mc /usr/bin/mc /bin/mc
COPY --from=kaniko /kaniko /kaniko

RUN echo "http://dl-cdn.alpinelinux.org/alpine/edge/community" >> /etc/apk/repositories \
  && apk add --update --virtual .dockerbuilder-rundeps \
    caddy \
    ca-certificates \
    bash \
  && pip3 install --disable-pip-version-check \
    --no-cache-dir \
    requests==2.24.0

CMD ["python3", "/deploy.py"]
