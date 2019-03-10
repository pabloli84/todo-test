from flask import Flask
from flask_restful import Resource, Api
import logging
# from server import db
import db

logger = logging.getLogger()
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s-%(levelname)-8s %(message)s')
handler.setFormatter(formatter)
handler.setLevel(logging.INFO)
logger.addHandler(handler)


logger.setLevel(logging.INFO)

base = db.ManageTodoDB("db.sqlite")
base.create_db_struct()
base.add_user("Michael")
base.add_task("Test 1", "This my first task", 1, "2019-03-10", "2019-03-11")
