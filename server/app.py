from flask import Flask
from flask_restful import Resource, Api
import logging
# from server import db
import db, resources

logger = logging.getLogger()
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s-%(levelname)-8s %(message)s')
handler.setFormatter(formatter)
handler.setLevel(logging.INFO)
logger.addHandler(handler)

logger.setLevel(logging.INFO)

app = Flask(__name__)
api = Api(app)

# base = db.ManageTodoDB("db.sqlite")
# base.create_db_struct()
# base.add_user("Michael")
# base.add_task("Test 1", "This my first task", 1, "2019-03-10", "2019-03-11")

# manage_todos = db.ManageTodoDB()

api.add_resource(resources.Tasks, '/tasks')
api.add_resource(resources.Users, '/users')


if __name__ == '__main__':
    app.run(debug=True)
