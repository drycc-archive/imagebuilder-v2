FROM minio/mc:RELEASE.2018-11-06T01-12-20Z as mc

FROM quay.io/drycc/base:v0.3.6

COPY . /
COPY --from=mc /usr/bin/mc /usr/bin/mc

RUN buildDeps='gcc git libffi-dev libssl-dev python3-dev python3-pip python3-wheel python3-setuptools'; \
    apt-get update && \
    apt-get install -y --no-install-recommends \
        $buildDeps \
        libffi6 \
        libssl1.0.0 \
        python3-minimal && \
	pip3 install --disable-pip-version-check --no-cache-dir docker-py==1.10.6 && \
    chmod +x /bin/get_object /bin/normalize_storage && \
    # cleanup
    apt-get purge -y --auto-remove $buildDeps && \
    apt-get autoremove -y && \
    apt-get clean -y && \
    rm -rf \
        /usr/share/doc \
        /usr/share/man \
        /usr/share/info \
        /usr/share/locale \
        /var/lib/apt/lists/* \
        /var/log/* \
        /var/cache/debconf/* \
        /etc/systemd \
        /lib/lsb \
        /lib/udev \
        /usr/lib/x86_64-linux-gnu/gconv/IBM* \
        /usr/lib/x86_64-linux-gnu/gconv/EBC* && \
    bash -c "mkdir -p /usr/share/man/man{1..8}"

CMD ["python3", "/deploy.py"]
