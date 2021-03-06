# todo-test

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