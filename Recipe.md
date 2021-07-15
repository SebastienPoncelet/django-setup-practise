
# Setup Django and project

- Check Django version
- Create project:
$ django-admin startproject <site_name>
- Create/choose virtual environment
- Check project is created properly by running the server:
$ python3 manage.py runserver
- Create app:
$ python3 manage.py startapp <app_name>
- Create simple view
- Declare url in app's URLconf
- Import URLconf in root urls.py
- Check if there are any issues by running the server:
$ python3 manage.py runserver
- If error, check if the url in the browser matches a declared url in the root url.py

# Setup the database and create models

## Setup the database

- In the project's settings.py, adjust the DATABASES.default values according to chosen database setup.
- Run migrations for the apps in the project settings.py, INSTALLED_APPS param:
$ python manage.py migrate

## Create models

- Create models
    _ Pay attention to each model's class name
    _ For a ForeignKey field, the related name is the current class' name. Name the parent will see its child/children
- Create migrations for the changes once all the models are created:
$ python3 manage.py makemigrations <app_name>
- Include app in the project settings.py, INSTALLED_APPS param. Path looks like:
'<app_name>.app.<app_class_name>'
- Check the SQL a specific migration would make:
$ python3 manage.py sqlmigrate <app_name> <migration_number>
- If it looks correct then run this command to apply all missing migrations in the DB:
$ python3 manage.py migrate
This command is to be used when models are modified without losing data