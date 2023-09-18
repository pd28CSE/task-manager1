# Task Manager



## Project Structure

```bash
.
└── task-manager1/
    ├── task_manager/                                     
    │   ├── __init__.py
    │   ├── asgi.py
    │   ├── settings.py                                              # project settings
    │   ├── urls.py                                                  # root URL
    │   └── wsgi.py
    ├── tasks/                                                       # app name
    │   ├── api/                                    
    │   │   ├── permissions.py                                       # custom permission
    │   │   ├── serializers.py                                       # serializers 
    │   │   ├── urls.py                                              # API ULS
    │   │   └── views.py                                             # API views
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── models.py                                                # Django Models class
    │   ├── views.py
    │   └── tests.py
    ├── media/                                                        # Media files 
    ├── fixtures/                                                     # dummy data 
    ├── manage.py
    ├── requirements.txt                                             # project dependency
    └── Task Manager Api Documentations.postman_collection.json      # API documentation

```



## Installations Process for Windows

1. At first need to install PostgreSQL if not already installed
2. Create the PostgreSQL database Name `taskmanager`
3. Create a USER `postgres`
4. Set the Password `password`
5. Set the Port `5432`

Install the virtual environment

    task-manager1> python -m venv env

Activate the virtual environment (env)

    task-manager1> env\Scripts\activate

Now, install the dependency inside the virtual environment

    (env) task-manager1> pip install -r requirements.txt

Migrate the Database

    (env) task-manager1> python manage.py makemigrations

Now Create the database tables

    (env) task-manager1> python manage.py migrate

After create database tables, Now load the dammy data in that database

    (env) task-manager1> python manage.py loaddata fixtures/tasklist.json

After complete the installation, now run the server

    (env) task-manager1> python manage.py runserver


## API Documentation include in `Task Manager Api Documentations.postman_collection.json` file
