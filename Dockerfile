FROM python:3.10

RUN set -eux; \
	apt-get update; \
    apt-get install sudo && \
	rm -rf /var/lib/apt/lists/*

RUN python3 -m pip install --upgrade pip && \
    python3 -m pip install duckdb==0.9.1

USER root
