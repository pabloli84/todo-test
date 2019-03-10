from flask_restful import Resource, reqparse, fields, marshal_with
import db

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
        dbase.add_task(args.task_name, args.description, args.assignee, args.start_date, args.end_date)

        return args, 201


class Users(Resource):

    def put(self):
        args = parser.parse_args()
        user_name = args['user_name']
        dbase.add_user(user_name)
        return user_name, 201
