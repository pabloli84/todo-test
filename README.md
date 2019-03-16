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
    
* /tasks
    * POST - create new task
    Sample json
    ```json
    {
        "task_name": "Task 9",
        "description": "This is Task 5",
        "assignee": "test user",
        "start_date": "2019-03-1333",
        "end_date": "2019-03-11 "
    }
    ```