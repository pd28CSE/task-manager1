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

## API Doc

### Create New User (POST Request) 

    http://127.0.0.1:8000/task-api/create-user/


Request Body

    {
        "first_name": "",
        "last_name":"",
        "username":"",
        "password":""
    }



### Login User (POST Request) 

    http://127.0.0.1:8000/task-api/


Request Body

    {
        "username":"",
        "password":""
    }



### Create User Task (POST Request) 

    http://127.0.0.1:8000/task-api/create-task/


Request Headers

    {
        "Content-Type":"multipart/form-data; boundary=<calculated when request is sent>",
        "Authorization":"Token <token>"
    }


Request Body

    {
        "title":"",
        "description":"",
        "dueDate":"",
        "priority":"",
        "isCompleted":"",
        "images": ['list of image']
    }



### Get User Task List (GET Request) 

    http://127.0.0.1:8000/task-api/user-task-list/


Request Headers

    {
        "Authorization":"Token <token>"
    }


Response Body

    [
        {
            "id": 33,
            "user": "mir",
            "title": "Why do we use it?",
            "description": "It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout.",
            "images": [
                {
                    "id": 42,
                    "image": "http://127.0.0.1:8000/medias/images/tai-bui-QW89whdEClA-unsplash_DqmVrGz.jpg"
                },
                {
                    "id": 43,
                    "image": "http://127.0.0.1:8000/medias/images/420120_uedYOZc.jpg"
                }
            ],
            "creationDateTime": "2023-09-18T14:56:13.947368+06:00",
            "dueDate": "2023-07-02",
            "priority": "High",
            "isCompleted": false
        },
    ]



### User Task Update (PUT Request) 

    http://127.0.0.1:8000/task-api/update-task/<task_id>/


Request Headers

    {
        "Content-Type":"multipart/form-data; boundary=<calculated when request is sent>",
        "Authorization":"Token <token>"
    }


Request Body

    {
        "title":"",
        "description":"",
        "dueDate":"",
        "priority":"",
        "isCompleted":"",
        "images": ['list of image']
    }



### User Task Delete (DELETE Request) 

    http://127.0.0.1:8000/task-api/delete-task/<task_id>/


Request Headers

    {
        "Authorization":"Token <token>"
    }



### Get Specific Task (GET Request) 

    http://127.0.0.1:8000/task-api/task-details/<task_id>/


Request Headers

    {
        "Authorization":"Token <token>"
    }

Response Body

    {
        "id": 33,
        "user": "mir",
        "title": "Why do we use it?",
        "description": "It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout.",
        "images": [
            {
                "id": 42,
                "image": "http://127.0.0.1:8000/medias/images/tai-bui-QW89whdEClA-unsplash_DqmVrGz.jpg"
            },
            {
                "id": 43,
                "image": "http://127.0.0.1:8000/medias/images/420120_uedYOZc.jpg"
            }
        ],
        "creationDateTime": "2023-09-18T14:56:13.947368+06:00",
        "dueDate": "2023-07-02",
        "priority": "High",
        "isCompleted": false
    }
