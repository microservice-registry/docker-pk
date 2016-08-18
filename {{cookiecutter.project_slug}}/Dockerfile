FROM python:3-onbuild
#WORKDIR /usr/src/app/
RUN python setup.py install
CMD [ "{{ cookiecutter.project_slug }}" ]
