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

# Project structure                                                     

```
[project_name]
├── LICENSE
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

The `project/` directory is the root of the actual Django project. All code files used by your application are inside this directory

| File or directory       | Purpose       | 
| ----------------------- | ------------- | 
| `config/`               | The configuration root of the project, where project-wide settings, `urls.py`, and `wsgi.py` modules are placed        | 
| `apps/`                 | Where you put your custom applications. When create your application from command line, remember to run the `startapp` command inside this directory| 
| `core/`                 | Where you put your generic solutions (helpers, views, middlewares, etc.) for common problems in a Django web application. If your code solve a common problem for any Django project, you should placed it here  |
| `static/`               | Non-user-generated static media assets including CSS, JavaScript, and images. |
| `templates/`            | Where you put your site-wide Django templates.    |
