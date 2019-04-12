FROM minio/mc:RELEASE.2018-11-06T01-12-20Z as mc
FROM gcr.io/kaniko-project/executor:v0.9.0 as kaniko

FROM python:3.7-alpine

COPY . /
COPY --from=mc /usr/bin/mc /usr/bin/mc
COPY --from=kaniko /kaniko /kaniko

ARG CADDY_VERSION=v0.11.5
RUN mkdir /tmp/caddy \
  && cd /tmp/caddy \
  && wget https://github.com/mholt/caddy/releases/download/${CADDY_VERSION}/caddy_${CADDY_VERSION}_linux_amd64.tar.gz \
  && tar -xvzf caddy_v0.11.5_linux_amd64.tar.gz \
  && cp /tmp/caddy/caddy /usr/bin \
  && rm -rf /tmp/caddy

RUN apk add --update --virtual .dockerbuilder-rundeps \
    ca-certificates \
    bash \
  && pip3 install --disable-pip-version-check \
    --no-cache-dir \
    requests==2.21.0

CMD ["python3", "/deploy.py"]
