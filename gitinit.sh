#!/bin/bash
git init
git add .
git remote add \
    origin https://github.com/microservice-projects/{{ cookiecutter.project_slug | replace("_", "-") }}
git push origin master
