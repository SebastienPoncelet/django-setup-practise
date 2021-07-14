
# Setup Django and project

- Check Django version
- Create project:
$ django-admin startproject <site_name>
- Create/choose virtual environment
- Check project is created properly by running the server:
$ python manage.py runserver
- Create app:
$ python manage.py startapp <app_name>
- Create simple view
- Declare url in app's URLconf
- Import URLconf in root urls.py
- Check if there are any issues by running the server:
$ python manage.py runserver
- If error, check if the url in the browser matches a declared url in the root url.py

# Setup the database and create models

## Setup the database

- In the project's settings.py, adjust the DATABASES.default values according to chosen database setup.
- Run migrations for the apps in the project settings.py, INSTALLED_APPS param:
$ python manage.py migrate

## Create models

- Include app in the project settings.py, INSTALLED_APPS param. Path looks like:
<app_name>.app.<app_class_name>

