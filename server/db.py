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
            logger.error('Error connecting to DB: %s', e)

    def close_db(self):
        self.db.close()

    def create_db_struct(self):
        sql = '''
            CREATE TABLE IF NOT EXISTS tasks (
                task_id INTEGER PRIMARY KEY AUTOINCREMENT,
                task_name VARCHAR(250) NOT NULL,
                task_description VARCHAR(1000) NOT NULL,
                task_assignee INTEGER NOT NULL,
                task_start_date DATE, task_end_date DATE,
                FOREIGN KEY (task_assignee) REFERENCES users(user_id)
            );
                 
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_name VARCHAR(50) NOT NULL
            );
              '''
        c = self.db.cursor()
        try:
            c.executescript(sql)
            logger.info("DB structure was created!")
        except sqlite3.Error as e:
            logger.error("Error creating DB: %s", e)
            return e

    def add_user(self, username):
        sql = '''
            INSERT INTO users (user_name) VALUES("{:s}")    
        '''.format(username)
        c = self.db.cursor()
        try:
            c.executescript(sql)
            logger.info("Successfully added user %s", username)
        except sqlite3.Error as e:
            logger.error("Error adding user %s. Message: %s", username, e)
            return e

    def add_task(self, name, description, assignee, start_date, end_date):
        sql = '''
            INSERT INTO tasks (task_name, task_description, task_assignee, task_start_date, task_end_date)
            VALUES("{:s}", "{:s}", {:d}, "{:s}", "{:s}")
        '''.format(name, description, assignee, start_date, end_date)

        c = self.db.cursor()
        try:
            c.executescript(sql)
            logger.info("Successfully added task: %s", name)
        except sqlite3.IntegrityError as e:
            logger.error("DB integrity error: %s", e)
            return e

    def remove_db(self):
        sql = '''
            DROP DATABASE;
        '''
        c = self.db.cursor()

        return c.executescript(sql)
