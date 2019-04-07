import os
import tarfile
import base64
import json
import requests
import subprocess

DEBUG = os.environ.get('DRYCC_DEBUG') in ('true', '1')
registryLocation = os.getenv('DRYCC_REGISTRY_LOCATION', 'on-cluster')


def log(msg):
    if DEBUG:
        print(msg)


def docker_login(username, password, registry):
    login_data = {
        "auths": {
            registry: {
                "auth": base64.b64encode(
                    ("%s:%s" % (username, password)).encode("utf8")).decode("utf8")
            }
        },
        "HttpHeaders": {
            "User-Agent": "Docker-Client/18.06.1-ce (linux)"
        }
    }
    os.makedirs("/root/.docker", exist_ok=True)
    with open("/root/.docker/config.json", "w") as fb:
        json.dump(login_data, fb)


def call_kaniko(dockerfile, context, destination, **kwargs):
    command = [
        "/kaniko/executor",
        "--dockerfile=%s" % dockerfile,
        "--context=%s" % context,
        "--destination=%s" % destination,
        "--insecure=%s" % kwargs.pop("insecure", "false"),
        "--insecure-registry=%s" % kwargs.pop("insecure_registry", "false"),
    ]
    command.extend([
        "--build-arg %s=%s" % item for item in kwargs.pop(
            "build_arg", {}).items()
    ])
    subprocess.check_call(command)


def get_registry_name():
    hostname = os.getenv('DRYCC_REGISTRY_HOSTNAME', "")
    insecure = "false" if hostname.startswith("https") else "true"
    if registryLocation == "off-cluster":
        organization = os.getenv('DRYCC_REGISTRY_ORGANIZATION')
        registry_name = ""
        # empty hostname means dockerhub and hence no need to prefix the image
        hostname = hostname.replace("https://", "").replace("http://", "")
        if hostname != "":
            registry_name = hostname + "/"
        # Registries may have organizations/namespaces under them which needs to
        # be prefixed to the image
        if organization != "":
            registry_name = registry_name + organization
    else:
        registry_name = "{}:{}".format(
            os.getenv("DRYCC_REGISTRY_SERVICE_HOST"),
            os.getenv("DRYCC_REGISTRY_SERVICE_PORT")
        )
    return insecure, registry_name


def download_file(tar_path):
    command = [
        "get_object",
        tar_path,
        "apptar"
    ]
    subprocess.check_call(command)


def main():
    tar_path = os.getenv('TAR_PATH')
    if tar_path:
        if os.path.exists("/var/run/secrets/drycc/objectstore/creds/"):
            download_file(tar_path)
        else:
            r = requests.get(tar_path)
            with open("apptar", "wb") as app:
                app.write(r.content)
    log("download tar file complete")
    with tarfile.open("apptar", "r:gz") as tar:
        tar.extractall("/app/")
    log("extracting tar file complete")
    buildargs = json.loads(os.getenv('DOCKER_BUILD_ARGS', '{}'))
    # inject docker build args into the Dockerfile so we get around Dockerfiles
    # that don't have things like PORT defined.
    with open("/app/Dockerfile", "a") as dockerfile:
        # ensure we are on a new line
        dockerfile.write("\n")
        for envvar in buildargs:
            dockerfile.write("ARG {}\n".format(envvar))
    if registryLocation != "on-cluster":
        registry = os.getenv('DRYCC_REGISTRY_HOSTNAME', 'https://index.docker.io/v1/')
        username = os.getenv('DRYCC_REGISTRY_USERNAME')
        password = os.getenv('DRYCC_REGISTRY_PASSWORD')
        docker_login(username=username, password=password, registry=registry)
    insecure, registry = get_registry_name()
    imageName, imageTag = os.getenv('IMG_NAME').split(":", 1)
    repo = registry + "/" + os.getenv('IMG_NAME')
    call_kaniko(
        "/app/Dockerfile",
        context="/app",
        destination=repo,
        insecure=insecure,
        insecure_registry=insecure,
    )


if __name__ == "__main__":
    main()
