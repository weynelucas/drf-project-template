# drf-project-template
A project template with common setups to start projects with Django + Django REST framework

# Features

-  Django 2.2+
-  Django REST framework 3.10+
-  Environment variables loading with [django-dotenv](https://github.com/jpadilla/django-dotenv)
-  Generating documentation from OpenAPI schemas with [drf-yasg](https://github.com/axnsan12/drf-yasg/)
-  CORS support with [django-cors-headers](https://github.com/adamchainz/django-cors-headers)
-  Exposing application information over [Browseable API](https://www.django-rest-framework.org/topics/browsable-api/)

# Installation

```bash
$ django-admin.py startproject \
  --template=https://github.com/weynelucas/drf-project-template/archive/master.zip \
  --extension=py,md,env,yml \
  project_name
$ cd project_name
$ pip install -r requirements.txt
```

# Describing your application
At the end of the `settings.py` you can describe your aplication (name, description and release version). Theese informations will be displayed inside documentation (Swagger and Redoc) and inside the navigation bar of the Browseable API 

```python
# settings.py

APP_VERSION = '1.0.0'
APP_NAME = 'Your project name'
APP_DESCRIPTION = 'Your project description'
```

# Configuring applications

This project template highly recommends Django apps to be placed inside `apps/` directory. To work with this configuration you need first to run the `startapp`command inside this directory:

```bash
$ cd project/apps
$ python ../manage.py startapp pools
```

After create the app folder, go to the `AppConfig` subclass (inside `apps.py`) and provide a proper name, wich is a dotted path to the application module:

```python
from django.apps import AppConfig


class PoolsConfig(AppConfig):
    name = 'apps.pools'
    
```

Inside `__init__.py` file inside your module, set the `default_app_config` variable with the dotted path to your `AppConfig` subclass:

```python
default_app_config = 'apps.pools.apps.PoolsConfig'
```

Finnaly, install your app using the configured dotted path:

```python
# settings.py

INSTALLED_APPS = [
  ...
  'apps.pools',
]
```

# Settings
You can setting your application with envinronment variables. Create a `.env` file inside the `project/` directory and set your environment variables, most variables names refer to [Django settings](https://docs.djangoproject.com/en/2.2/ref/settings/). 

## Core settings

| Variable        | Description                                                                          | Default   |
| --------------- | ------------------------------------------------------------------------------------ | :-------: |
| `DEBUG`         | Turns on/off debug mode. Never deploy a site into production with `DEBUG` turned on  | `true`    |
| `ALLOWED_HOSTS` | List, splitted by comma, of host/domain that your application can serve               | `*`       |
| `PROXY_SCRIPT_NAME` | If the app is running behind a proxy, this variable must be set with the proxy path | -      |


#### Example
```
DEBUG=True
ALLOWED_HOSTS=www.example.com,.subdomain.com
PROXY_SCRIPT_NAME=/api
```

## Database settings
To know how configure databases in a Django application, see the [documentation](https://docs.djangoproject.com/en/2.2/ref/databases/)


| Variable         | Description                                                                          | Default     |
| ---------------  | ------------------------------------------------------------------------------------ | :---------: |
| `DB_ENGINE`      | Database backend to use. Options are: `mysql`, `oracle`, `postgresql`, `postgresql_psycopg2`,  `sqlite3`         | `sqlite3`    |
| `DB_NAME`        | The name of database to use                                                          | `db.sqlite3`|
| `DB_HOST`        | Which host to use when connecting to the database                                    | -           |
| `DB_PORT`        | The port to use when connecting to the database                                      | -           |
| `DB_USER`        | The username to use when connecting to the database                                  | -           |
| `DB_PASSWORD`    | The password to use when connecting to the database                                  | -           |
| `DB_CONN_MAX_AGE`| The lifetime of a database connection, in seconds                                    | `0`         |

Depending on your `DB_ENGINE` variable you should install another package like `psycopg2` or `cx_Oracle` for PostgreSQL and Oracle databases, respectively.

#### Example

```
# PostgreSQL settings
DB_ENGINE=postgresql_pyscopg2
DB_NAME=database
DB_HOST=localhost
DB_PORT=27017
DB_USER=a_user
DB_PASSWORD=a_password

# Oracle settings (connect using SID)
DB_ENGINE=oracle
DB_NAME=xe
DB_HOST=dbprod01ned.mycompany.com
DB_PORT=1540
DB_USER=a_user
DB_PASSWORD=a_password

# Oracle settings (connect using full DSN string)
DB_ENGINE=oracle
DB_NAME=(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVICE_NAME=orclpdb1)))
DB_HOST=
DB_PORT=
DB_USER=a_user
DB_PASSWORD=a_password

# Oracle settings (connect using Easy Connect string)
DB_ENGINE=oracle
DB_NAME=localhost:1521/orclpdb1
DB_HOST=
DB_PORT=
DB_USER=a_user
DB_PASSWORD=a_password
```


# Project structure                                                     

```
[project_name]
├── docker
│   ├── docker-compose.dev.yml
│   └── Dockerfile
├── environments
│   ├── environment.dev.env
│   ├── environment.prod.env
│   └── environment.stage.env
├── project
│   ├── apps
│   │   └── __init__.py
│   ├── config
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── core
│   ├── manage.py
│   ├── static
│   └── templates
│       └── rest_framework
│           └── api.html
├── README.md
└── requirements.txt
```

The `docker/` directory is where are the configuration files needed to run the application with docker.

The `environments/` contains `.env` samples for development, stage and production environments.

The `project/` directory is the root of the actual Django project. All code files used by your application are inside this directory

| File or directory       | Purpose       | 
| ----------------------- | ------------- | 
| `config/`               | The configuration root of the project, where project-wide settings, `urls.py`, and `wsgi.py` modules are placed        | 
| `apps/`                 | Where you put your custom applications. When create your application from command line, remember to run the `startapp` command inside this directory| 
| `core/`                 | Where you put your generic solutions (helpers, views, middlewares, etc.) for common problems in a Django web application. If your code solve a common problem for any Django project, you should placed it here  |
| `static/`               | Non-user-generated static media assets including CSS, JavaScript, and images. |
| `templates/`            | Where you put your site-wide Django templates.    |
