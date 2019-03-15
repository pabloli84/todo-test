from flask_restful import Resource, reqparse, fields, marshal_with
from modules import db
import logging

logger = logging.getLogger()

dbase = db.ManageTodoDB()

parser = reqparse.RequestParser()
parser.add_argument('task_name', dest='task_name')
parser.add_argument('description', dest='description')
parser.add_argument('assignee', dest='assignee')
parser.add_argument('start_date', dest='start_date')
parser.add_argument('end_date', dest='end_date')
parser.add_argument('user_name')

task_fields = {
    "task_name": fields.String,
    "description": fields.String,
    "assignee": fields.String,
    "start_date": fields.String,
    "end_date": fields.String
}


class Tasks(Resource):

    @marshal_with(task_fields)
    def put(self):
        args = parser.parse_args()
        response = dbase.add_task(args.task_name, args.description, args.assignee, args.start_date, args.end_date)

        return args, response

    def get(self):
        return dbase.get_all_tasks()


class Users(Resource):

    def put(self):
        args = parser.parse_args()
        user_name = args['user_name']
        if dbase.add_user(user_name):
            return user_name, 201
        else:
            return "Data integrity error", 400

    def get(self):
        logger.info("Getting all users from DB")
        return dbase.get_all_users()


class TasksDB(Resource):
    def delete(self):
        dbase.recreate_db()
        return '', 204
