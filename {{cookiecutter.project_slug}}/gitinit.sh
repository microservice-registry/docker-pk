#!/bin/bash
git init
git add .
git commit -am "first commit"
git remote add \
    origin https://github.com/microservice-projects/{{ cookiecutter.project_slug | replace("_", "-") }}
git push origin master
