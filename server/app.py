from flask import Flask
from flask-restful import Resource, Api
import logging
import db

logger = logging.getLogger()
formatter = logging.Formatter('%(asctime)s-%(levelname)-8s %(message)s')
logger.setFormatter(formatter)

logger.setLevel(logging.INFO)

base = db.ManageTodoDB("db.sqlite")
base.create_db_struct()