#!/bin/bash

# Building the images
docker-compose build

# Running the tests
docker-compose up

# Tear down the setup after tests
docker-compose down
