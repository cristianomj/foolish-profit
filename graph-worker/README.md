# Graph Worker

This is a simple python worker which reads from NATS and generates historical graphs of stock prices, storing the resulting artifacts in S3 (minio in local development).

We use [poetry](https://python-poetry.org) for dependency management.

