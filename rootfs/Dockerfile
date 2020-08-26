FROM gcr.io/kaniko-project/executor:v0.24.0 as kaniko

FROM python:3.8-alpine

COPY . /
COPY --from=kaniko /kaniko /kaniko

RUN wget https://dl.min.io/client/mc/release/linux-amd64/mc -O /bin/mc \
  && chmod +x /bin/mc \
  && mkdir /tmp/caddy \
  && cd /tmp/caddy \
  && wget https://github.com/caddyserver/caddy/releases/download/v2.1.1/caddy_2.1.1_linux_amd64.tar.gz \
  && tar -xvzf caddy_2.1.1_linux_amd64.tar.gz \
  && cp /tmp/caddy/caddy /usr/bin \
  && rm -rf /tmp/caddy

RUN apk add --update --virtual .dockerbuilder-rundeps \
    ca-certificates \
    bash \
  && pip3 install --disable-pip-version-check \
    --no-cache-dir \
    requests==2.24.0

CMD ["python3", "/deploy.py"]
