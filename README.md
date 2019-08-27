# drf-project-template
A project template with common setups to start projects with Django + Django REST framework

# Features

-  Django 2.2+
-  Django REST framework 3.10+
-  Generating documentation from OpenAPI schemas with [drf-yasg](https://github.com/axnsan12/drf-yasg/)
-  CORS support with [django-cors-headers](https://github.com/adamchainz/django-cors-headers)

# Installation

```bash
$ django-admin.py startproject \
  --template=https://github.com/weynelucas/drf-project-template/archive/master.zip \
  --extension=py,md,env \
  project_name

$ cd project_name
$ pip install -r requirements.txt
```