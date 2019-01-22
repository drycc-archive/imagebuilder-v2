
# Drycc Dockerbuilder v2

[![Build Status](https://ci.drycc.cc/job/dockerbuilder/badge/icon)](https://ci.drycc.cc/job/dockerbuilder)
[![codebeat badge](https://codebeat.co/badges/b9039897-fef4-4950-bac8-94503394e6c2)](https://codebeat.co/projects/github-com-drycc-dockerbuilder)
[![Docker Repository on Quay](https://quay.io/repository/drycc/dockerbuilder/status "Docker Repository on Quay")](https://quay.io/repository/drycc/dockerbuilder)

Drycc (pronounced DAY-iss) Workflow is an open source Platform as a Service (PaaS) that adds a developer-friendly layer to any [Kubernetes](http://kubernetes.io) cluster, making it easy to deploy and manage applications on your own servers.

For more information about the Drycc Workflow, please visit the main project page at https://github.com/drycc/workflow.

We welcome your input! If you have feedback, please [submit an issue][issues]. If you'd like to participate in development, please read the "Development" section below and [submit a pull request][prs].

[issues]: https://github.com/drycc/workflow/issues
[prs]: https://github.com/drycc/workflow/pulls

# About

The Dockerbuilder downloads a git archive ([gzip](http://www.gzip.org/)ped [tar](https://www.gnu.org/software/tar/)ball) from a specified [S3 API compatible server][s3-api] and runs `docker build` on it. When the build is done, it runs `docker push` to push the resulting image to a specified [Docker](https://www.docker.com/) repository.

This component is usually launched by the [Drycc Builder](https://github.com/drycc/builder) and used inside the Drycc [PaaS](https://en.wikipedia.org/wiki/Platform_as_a_service), but it is flexible enough to be used as a pod inside any Kubernetes cluster.

# Development

The Drycc project welcomes contributions from all developers. The high level process for development matches many other open source projects. See below for an outline.

* Fork this repository
* Make your changes
* [Submit a pull request][prs] (PR) to this repository with your changes, and unit tests whenever possible.
  * If your PR fixes any [issues][issues], make sure you write Fixes #1234 in your PR description (where #1234 is the number of the issue you're closing)
* The Drycc core contributors will review your code. After each of them sign off on your code, they'll label your PR with LGTM1 and LGTM2 (respectively). Once that happens, the contributors will merge it

[issues]: https://github.com/drycc/workflow/issues
[prs]: https://github.com/drycc/workflow/pulls
[v2.18]: https://github.com/drycc/workflow/releases/tag/v2.18.0
