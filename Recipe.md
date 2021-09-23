
# Setup Django and project

- Create project:
$ django-admin startproject <site_name>
- Create/choose virtual environment following 3.a steps:
- Check Django version.
- Check project is created properly by running the server:
$ python3 manage.py runserver
- Select virtual environment in VS code's interpreter:
https://stackoverflow.com/questions/53007637/e0401unable-to-import-django-db
- Create app:
$ python3 manage.py startapp <app_name>
- Add app to project's settings.py 'INSTALLED_APPS' array.
'<app_name>.apps.<AppNameConfig>'
where <AppNameConfig> is the class name in the <app_name> apps.py.
- Check project is created properly by running the server:
$ python3 manage.py runserver
- Create models according to section 1.
- Create super user for django admin:
$ python manage.py createsuperuser
- Register models in <app_name> admin.py to allow admin interface. 
- Install and setup JWT according to section 5.
- Create views according to section 3.
- Declare url in app's URLconf
- Import URLconf in root urls.py
- Check if there are any issues by running the server:
$ python3 manage.py runserver
- If error, check if the url in the browser matches a declared url in the root url.py

# 1 Setup the database and create models

## a Setup the database

- In the project's settings.py, adjust the DATABASES.default values according to chosen database setup.
- Indicate changes to models:
$ python manage.py makemigrations
- Run migrations:
$ python manage.py sqlmigrate <app_name> <migration_number>
- Run migrations for the apps in the project settings.py, INSTALLED_APPS param:
$ python manage.py migrate

## b Create models

- Create models
    - Pay attention to each model's class name
    - For a ForeignKey field, the related name is the current class' name. Name the parent will see its child/children
    - Do not forget to declare any on delete cascade for children model fields in parent models.
- Create migrations for the changes once all the models are created:
$ python3 manage.py makemigrations <app_name>
- Include app in the project settings.py, INSTALLED_APPS param. Path looks like:
'<app_name>.app.<app_class_name>'
- Check the SQL a specific migration would make:
$ python3 manage.py sqlmigrate <app_name> <migration_number>
- If it looks correct then run this command to apply all missing migrations, all changes, in the DB:
$ python3 manage.py migrate
This command is to be used when models are modified without losing data

## c If using Django's auth user model
- Don't forget to declare your User model in the settings as:
$ AUTH_USER_MODEL = '<app_nam>.<user_model_class_name>'

# 2 Setup the Django admin system
- Create a super user:
$ python3 manage.py createsuperuser
- Access to Django's admin panel by entering the following URL in the browser:
<domain>/admin/
- Register model objects to tell the admin it has an admin interface. File to update:
<app_name>/admin.py

# 3 Create the views (controllers) and the serializers (views/templates)

## a Prerequesite setup

- Use a virtual environment to make sure that the package configuration is kept nicely isolated from any other projects.
Sources:
https://www.django-rest-framework.org/tutorial/1-serialization/
https://stackoverflow.com/questions/1534210/use-different-python-version-with-virtualenv/39713544#39713544
https://docs.python.org/3/library/venv.html
- Create the environment in python 3 with the following command:
$ python3 -m venv <env_name>
- Define the path where to activate the virtual environment:
$ source <env_name>/<path_to_environment>
example:
$ source env/bin/activate
(activate is created)
- Deactivate the virtual environment with:
$ deactivate
- Install Django in newly created virtual environment if necessary.
$ pip3 install Django
- Install Django Rest Framework in the virtual environment:
$ pip3 install djangorestframework
- Add the rest_framework app to INSTALLED_APPS in the <app_name>/settings.py file.

## b Create views
- If views are split in multiple files:
    - Create a <views> folder.
    - Create 1 view file per view.
    - Import all view files in <site_name>/<app_name>/views/__init__.py
- If using class based views and ViewSets, 1 view <--> 1 model.

## c Create serializers
- Use ModelSerializer to keep the code concise.
- If using class based views and ViewSets:
    - 1 ViewSets <--> 1 ModelSerializer for all CRUD actions.
    - 1 url <--> 1 ViewSets for all CRUD endpoints.


## d Setup the corresponding urls
- Register a view in the <site_name>/<app_name>/urls.py


# 4 Typical errors
-  'Indentation Error: unindent does not match any outer indentation level'
--> there's a mix of tabs and spaces somewhere in the file.
- Create the __str__() model instance method to help identify entities more easily.


#TODO
- Complete creating serializers and views (test creating nested objects in same request)
- Setup the user model with Django's authentication.
- Setup the Django Rest framework JWT authentication.
- Create unit tests.
- Create permissions based on user access and HTTP request type (GET, POST etc.).
- Create proper DB with either PostgreSQL or MySQL according to Django's documentation.
- Create a server to host this project (nginx?) or host on Heroku for practise.
- Setup Docker.

# 5 Authentication Token
- Can use djangorestframework-simplejwt librairy as it's popular and regularly updated:
https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html
https://github.com/jazzband/djangorestframework-simplejwt
- Install in virtual environment:
$ pip3 install djangorestframework-simplejwt
- Add this librairy in the settings.py file by adding this whole section:
```REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}
```
