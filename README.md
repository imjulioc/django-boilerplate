Template for deploying django projects with docker, nginx, gunicorn and postgres

By dedault web service installs python dependencies based on [requeriments.pip](https://github.com/imjulioc/django-project-template/blob/master/src/requirements.pip) which does not specify any version (so last dependencie version would be downloaded).

## Debugging and develop django project
Run your django project by not building anything yet setting a venv inside [src](https://github.com/imjulioc/django-project-template/tree/master/src) and running **django runserver** command with **--settings='project.local_settings'** parameter.

## Useful commands
- make build: build services from docker-compose
- make start: starts services
- make stop: stops services
- make restart: restarts services
- make collectstatic: invoke django-collectstatic command in web service
- make createsuperuser username=USERNAME email=EMAIL password=PASSWORD: invoke django-createsuperuser command in webservice. Parameters must be single quoted.
- make createlocalsuperuser: similar usage to createsuperuser. Parameters must be single quoted.

Also see Makefile for commands complete list.
