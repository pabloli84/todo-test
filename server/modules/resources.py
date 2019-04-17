from flask_restful import Resource, reqparse, fields, marshal_with, abort
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
parser.add_argument('status', dest='status')
parser.add_argument('user_name')

task_fields = {
    "task_name": fields.String,
    "description": fields.String,
    "assignee": fields.String,
    "start_date": fields.String,
    "end_date": fields.String,
    "status": fields.String
}


class Tasks(Resource):

    # Create task
    @marshal_with(task_fields)
    def post(self):
        args = parser.parse_args(strict=True)
        response, code = dbase.add_task(args.task_name, args.description, args.assignee, args.start_date, args.end_date)
        if code != 201:
            abort(code, description=response)
        return args, code

    def get(self):
        return dbase.get_all_tasks()


class Task(Resource):

    def get(self, task_id):
        return dbase.get_task_by_id(task_id)

    def delete(self, task_id):
        if dbase.delete_task(task_id):
            return "", 204
        else:
            return {"message": "Data integrity error!"}, 400

    # Update task
    @marshal_with(task_fields)
    def put(self, task_id):
        args = parser.parse_args(strict=True)

        if dbase.update_task(task_id=task_id, task_name=args.task_name,
                             task_descripiton=args.description,
                             task_assignee=args.assignee,
                             status=args.status if args.status is not None else "none"):
            return "Successfully updated task {:s}".format(args.task_name), 204
        else:
            return "Data integrity error!", 400


class Users(Resource):

    def post(self):
        args = parser.parse_args()
        user_name = args['user_name']
        if dbase.add_user(user_name):
            return user_name, 201
        else:
            return "Data integrity error", 400

    def get(self):
        logger.info("Getting all users from DB")
        return dbase.get_all_users()


class User(Resource):
    def delete(self, user_name):

        if dbase.delete_user(user_name):
            return "", 204
        else:
            return "Data integrity error", 400


class TasksDB(Resource):
    def delete(self):
        dbase.recreate_db()
        return '', 204
