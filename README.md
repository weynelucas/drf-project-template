# drf-project-template
A project template with common setups to start projects with Django + Django REST framework

# Features

-  Django 2.2+
-  Django REST framework 3.10+
-  Environment variables loading with [django-dotenv](https://github.com/jpadilla/django-dotenv)
-  Generating documentation from OpenAPI schemas with [drf-yasg](https://github.com/axnsan12/drf-yasg/)
-  CORS support with [django-cors-headers](https://github.com/adamchainz/django-cors-headers)
-  Exposing versioning information

# Installation

```bash
$ django-admin.py startproject \
  --template=https://github.com/weynelucas/drf-project-template/archive/master.zip \
  --extension=py,md,env \
  project_name
$ cd project_name
$ pip install -r requirements.txt
```

# Environment variables

All available settings with their respective example values are:

```
# Core settings
DEBUG=false
PROXY_SCRIPT_NAME=api
ALLOWED_HOSTS=localhost,127.0.0.1,example.com
SECRET_KEY=10$)=r1sb!uuf6(b6-_!ogs=*73)(roh^h2!4f1!l8%@-kt4bh

# Database
DB_ENGINE=postgres_psycopg2 # Allowed options: sqlite3, mysql, postgresql, postgresql_psycopg2, oracle
DB_NAME=database_name
DB_HOST=localhost
DB_PORT=27017
DB_USER=postgres
DB_PASSWORD=postgres

# Static files
STATIC_PATH=/static/
STATIC_URL=http://static.example.com/ # If not provided, value will be set to PROXY_SCRIPT_NAME + STATIC_PATH
STATIC_ROOT=/www/static/

# CORS
CORS_ALLOW_ORIGIN_ALL=false
CORS_ORIGIN_WHITELIST=https://example.com,https://sub.example.com
CORS_ORIGIN_REGEX_WHITELIST='https://\w+\.example\.com$
```