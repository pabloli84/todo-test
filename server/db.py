import sqlite3
import logging

logger = logging.getLogger()


class ManageTodoDB:

    db = sqlite3.Connection

    def __init__(self, db_file):
        self.db_file = db_file
        self.connect()

    def connect(self):
        try:
            self.db = sqlite3.connect(self.db_file)
            logger.info("Connected to DB: %s", self.db_file)
        except sqlite3.Error as e:
            logger.error('Error connecting to DB: %s', e.message)

    def close_db(self):
        self.db.close()

    def create_db_struct(self):
        sql = '''
            CREATE TABLE IF NOT EXISTS tasks (
                task_id INTEGER PRIMARY KEY AUTOINCREMENT,
                task_name VARCHAR(250) NOT NULL,
                task_description VARCHAR(1000) NOT NULL,
                task_assignee INT NOT NULL,
                task_start_data DATE, task_end_date DATE,
                FOREIGN KEY (task_assignee) REFERENCES (user_id)
            );
                 
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_name VARCHAR(50) NOT NULL
            );
              '''

        try:
            self.db.execute(sql)
        except sqlite3.Error as e:
            logger.error("Error creating DB: %s", e.message)
            return e
