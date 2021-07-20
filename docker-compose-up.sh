#!/usr/bin/env bash

docker-compose -f ./docker-compose.yaml build --no-cache

docker-compose up
