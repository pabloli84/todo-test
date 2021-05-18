Table of Contents
=================

   * [Setup and run](#setup-and-run)
   * [Setup with virtual env (recommended)](#setup-with-virtual-env-recommended)
   * [With Docker](#with-docker)
   * [API](#api)

# Setup and run

* Install python3 and pip3
* Install dependencies

```bash
pip install -r requirements.txt
```

* Run server:

```bash
cd ./server
python3 app.py
```

# Setup with virtual env (recommended)

* Install virtualenv

```
python3 -m pip install virtualenv
```

* Activate virtual env and install dependencies

```
cd todo-test
virtualenv -p python3 ./.venv
source ./.venv/bin/activate
pip3 install -r requirements.txt
```

* Activate virtual env on Windows

```
.\.venv\Scripts\activate.bat

```

* Run server

```
cd ./server
python3 app.py
```

# With Docker

Run following commands:

```
docker build -t todo-test:v0.1 .       
docker run -d --rm -p 5001:5001 todo-test:v0.1
```

# API

* /users
    * POST - create new user
    Sample Json
    ```json
    {"user_name": "test user"}
    ```
    * GET - get all users

* /users/<string:user_name>
    * DELETE - delete user with _user_name_

* /tasks
    * POST - create new task
    Sample json
    ```json
    {
        "task_name": "Task 9",
        "description": "This is Task 5",
        "assignee": "test user",
        "start_date": "2019-03-13",
        "end_date": "2019-03-11"
    }
    ```
    * GET - get all tasks

* /tasks/<int:task_id>
    * DELETE - delete task with _task_id_
    * PUT - update task, example Json:
    ```json
    {
      "task_name": "Task 9999999",
      "description": "This is Task 59999999",
      "assignee": "3000"
    }
    ```
    * GET - get task by _task_id_

* /db
    * DELETE - will delete all tables and recreate from scratch
