{% set is_open_source = cookiecutter.open_source_license != 'Not open source' -%}
# {{ cookiecutter.project_name }}

{{ cookiecutter.project_short_description }}

{% if is_open_source %}
* Free software: {{ cookiecutter.open_source_license }}
* Documentation: https://github.com/microservice-projects/{{ cookiecutter.project_slug | replace("_", "-") }}
{% endif %}

## Usages
Get
```shell
docker pull 4383/{{ cookiecutter.project_slug | replace("_","-") }}:latest
```

Run
```shell
docker run 4383/{{ cookiecutter.project_slug | replace("_","-") }}:latest
```

## Features

* {{ cookiecutter.features }}

## Credits

This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter)
and the [microservice-registry/docker-pk](https://github.com/microservice-registry/docker-pk) project template.
