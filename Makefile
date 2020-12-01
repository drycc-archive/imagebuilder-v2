SHORT_NAME := dockerbuilder
DRYCC_REGISTRY ?=
IMAGE_PREFIX ?= drycc
PLATFORM ?= linux/amd64,linux/arm64

include versioning.mk

DEV_ENV_IMAGE := drycc/python-dev
DEV_ENV_WORK_DIR := /app
DEV_ENV_PREFIX := docker run --rm -v ${CURDIR}/rootfs:${DEV_ENV_WORK_DIR} -w ${DEV_ENV_WORK_DIR}
DEV_ENV_CMD := ${DEV_ENV_PREFIX} ${DEV_ENV_IMAGE}

# For cases where we're building from local
docker-build:
	docker build ${DOCKER_BUILD_FLAGS} -t ${IMAGE} rootfs
	docker tag ${IMAGE} ${MUTABLE_IMAGE}

docker-buildx:
	docker buildx build --platform ${PLATFORM} ${DOCKER_BUILD_FLAGS} -t ${IMAGE} rootfs --push

test: test-style test-functional

test-style:
	${DEV_ENV_CMD} flake8 --show-source --config=setup.cfg .

test-functional:
	@echo "Implement functional tests in _tests directory"

.PHONY: all docker-build test test-style test-functional
