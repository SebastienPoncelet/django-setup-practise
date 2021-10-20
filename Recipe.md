
# Setup Django and project

- Create project:
$ django-admin startproject <site_name>
- Create/choose virtual environment following steps from section 1:
- Check Django version with the following command:
`$ python3 -m django --version`
- Check project is created properly by running the server (unapplied migrations are normal at this stage):
`$ python3 manage.py runserver`
- Select virtual environment in VS code's interpreter:
https://stackoverflow.com/questions/53007637/e0401unable-to-import-django-db
- Create app:
$ python3 manage.py startapp <app_name>
- Add app to project's settings.py 'INSTALLED_APPS' array.
'<app_name>.apps.<AppNameConfig>'
where <AppNameConfig> is the class name in the <app_name> apps.py.
- Check project is created properly by running the server:
$ python3 manage.py runserver
- Migrate the DB for the first time according to section 3.
- Create models according to section 2.
- Register models in <app_name> admin.py to allow admin interface. 
- Migrate the DB according to section 3.
- Setup the django admin according to section 4.
- Install and setup JWT according to section 5.
- Create views according to section 3.
- Declare url in app's URLconf
- Import URLconf in root urls.py
- Check if there are any issues by running the server:
$ python3 manage.py runserver
- If error, check if the url in the browser matches a declared url in the root url.py


# 1 Create and use a virtual environment

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
$ source <env_name>/bin/activate
(activate is created)
- Deactivate the virtual environment with:
$ deactivate
- Install Django in newly created virtual environment if necessary.
$ pip3 install Django
- Install Django Rest Framework in the virtual environment:
$ pip3 install djangorestframework
- Add the 'rest_framework' app to INSTALLED_APPS in the <app_name>/settings.py file.

# 2 Create models

## a Default process

- Create models
- Pay attention to each model's class name
- For a ForeignKey field, the related name is the current class' name. Name the parent will see its child/children
- Do not forget to declare any on delete cascade for children model fields in parent models.
- Modify the settings.py 'AUTH_USER_MODEL' with the proper user group name:
AUTH_USER_MODEL = '<app_name>.<customized_user_model_name>
- Create migrations for the changes once all the models are created:
$ python3 manage.py makemigrations <app_name>
- Include app in the project settings.py, INSTALLED_APPS param. Path looks like:
'<app_name>.app.<app_class_name>'
- Check the SQL a specific migration would make:
$ python3 manage.py sqlmigrate <app_name> <migration_number>
- If it looks correct then run this command to apply all missing migrations, all changes, in the DB:
$ python3 manage.py migrate
This command is to be used when models are modified without losing data

## b If using Django's auth user model
- Don't forget to declare your User model in the settings as:
$ AUTH_USER_MODEL = '<app_nam>.<user_model_class_name>'

## c Creating fixtures
- Create the corresponding folder and file:
<site_name>/<app_name>/fixtures/database.json
- Can create separate fixture files to make modifications easier to handle at:
<site_name>/<app_name>/fixtures/separated_fixtures/<model_name_plural>.json


# 3 Migrate the database

- In the project's settings.py, adjust the DATABASES.default values according to chosen database setup.
- Indicate changes to models:
$ python3 manage.py makemigrations
- Run migrations:
$ python3 manage.py sqlmigrate <app_name> <migration_number>
- Run migrations for the apps in the project settings.py, INSTALLED_APPS param:
$ python3 manage.py migrate
- Create fixtures according to step 1.d
- If fixtures don't need to hash any user password, enter the following command to populate the database:
$ python3 manage.py loaddata <fixture_file_name.extension>
- If fixtures don't need to hash any user password, create a custom command to hash user passwords in the DB when loading the fixtures by following this post:
https://stackoverflow.com/questions/8017204/users-in-initial-data-fixture
$ python3 manage.py <new_command_file_name_no_extension>


# 4 Setup the Django admin system
- Create a super user:
$ python3 manage.py createsuperuser
- Access to Django's admin panel by entering the following URL in the browser:
<domain>/admin/
- Register model objects to tell the admin it has an admin interface. File to update:
<app_name>/admin.py

# 3 Create the views (controllers) and the serializers (views/templates)



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
- If the fixtures have been changed, then delete the local database or loading the fixtures will create
unique constraint issues, trying to create objects with id numbers that already exist.


#TODO
- Complete creating serializers and views (test creating nested objects in same request)
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

# 6 Multi Language
- Check that the following has been installed (takes quite some time):
$ brew install gettext
$ brew link --force gettext
- In settings.py modify the 'LANGUAGE_CODE' to a generic one like 'en'.
- Import 'gettext_lazy' in settings.py like this:
from django.utils.translation import gettext_lazy as _
- If only a few supported languages are required, then specify them in the settings.py as follows,
otherwise all supported languages will be imported by Django:
LANGUAGES = (
    ('en', _('English')),
    ('<language_code>', _('<language_name>'))
)
- In settings.py 'MIDDLEWARE' add the corresponding middlewar in this order to user session data and
resolve the requested URL with the active language:
MIDDLEWARE = [
'django.contrib.sessions.middleware.SessionMiddleware',
'django.middleware.locale.LocaleMiddleware', # new
'django.middleware.common.CommonMiddleware',
]
- In settings.py define the path for locale files, at the project's root (using name 'locale' can be problematic):
LOCALE_PATHS = [
    BASE_DIR / 'locale/',
]
- Create the following folders at the 'LOCAL_PATHS' corresponding path (using name 'locale' can be problematic):
<project_root>/locale/<language_code_1>
<project_root>/locale/<language_code_2>
etc.
- Create a .po message file for each language
$ django-admin makemessages --all --ignore=env
- Once translations have been provided in the .po files, compile with the following command:
$ django-admin compilemessages --ignore=env
- Before running 

# 7 Unit test
- Install coverage with following command:
$ pip3 install coverage
- Run tests at level 2 with following command:
coverage run manage.py test <app_name> -v 2
- Remove the default tests.py file located at <project_name>/<main_app_name>/tests.py
- Create a 'tests' forlder at:
<app_name>/tests
- Don't forget to create the '__init__.py' file in this folder and subfolders.
- 1 test file <----> 1 test class <----> 1 setUp method.
Cannot have multiple classes each with their own 'setUp' method in the same folder

# 8 Setup Docker
- Get the list of packages for the application and save them in a 'requirements.txt' file:
$ pip3 freeze > requirements.txt
- Create Dockerfile in project's root.
- Build image to download required packages with command:
$ docker build --tag <image_wished_name> <directory_to_build>
$ docker build --tag python-django-test .
'.' designs the current directory
- Run the image and publish, link local and container ports, with command:
$ docker run --publish <local_port>:<container_port_from_Dockerfile> <tag_name_if_any>
$ docker run --publish 8000:8000 python-django-test
