import sqlite3
import logging
from datetime import datetime, timedelta, date

logger = logging.getLogger()

db_file = 'db.sqlite'


class ManageTodoDB:

    def connect_db(self):
        try:
            db = sqlite3.connect(db_file)
            logger.info("Connected to DB: %s", db_file)
            return db
        except sqlite3.Error as e:
            logger.error('Error connecting to DB: %s', e)

    # Create tables
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
                user_name VARCHAR(50) NOT NULL UNIQUE
            );
        '''
        c = self.connect_db().cursor()
        try:
            c.executescript(sql)
            logger.info("DB structure was created!")
        except sqlite3.Error as e:
            logger.error("Error creating DB: %s", e)
            return e

    # Add new user
    def add_user(self, username):
        sql = '''
            INSERT INTO users (user_name) VALUES("{:s}")    
        '''.format(username)
        c = self.connect_db().cursor()
        try:
            c.executescript(sql)
            logger.info("Successfully added user %s", username)
            return True
        except sqlite3.IntegrityError as e:
            logger.error("Error adding user %s. Message: %s", username, e)
            return False

    def delete_user(self, username):
        sql = '''
            DELETE FROM users WHERE user_name = "{:s}";
        '''.format(username)

        c = self.connect_db().cursor()
        try:
            c.executescript(sql)
            logger.info("Successfully deleted user %s", username)
            return True
        except sqlite3.IntegrityError as e:
            logger.error("Error deleting user %s. Message: %s", username, e)
            return False

    # Add new task
    def add_task(self, name, description, assignee, start_date, end_date):

        user_id = self.__get_user_id(assignee)
        if not user_id:
            return 404

        # =====Check dates validity==================================================
        now = datetime.now()
        s_date = datetime.strptime(start_date, "%Y-%m-%d")
        e_date = datetime.strptime(end_date, "%Y-%m-%d")

        if s_date.date() < now.date():
            message = "Start must be greater than or equal to now."
            logger.error(message)
            return {"message": message}, 400
        elif s_date > e_date:
            message = "Start date must be greater than equal to end date."
            logger.error(message)
            return {"message": message}, 400

        # =====Adjust dates according to technical task==============================
        if s_date.month == 2:
            e_date += timedelta(days=7)
            logger.warning("Start date is in Feb, so adding 7 days to end date: %s", e_date.strftime("%Y-%m-%d"))
        elif s_date.month == 12:
            e_date = date(s_date.year, s_date.month, 31)
            logger.warning("Start date is Dec, so setting end date to Dec 31st: %s", e_date.strftime("%Y-%m-%d"))
        elif s_date.month == 5:
            e_date += timedelta(days=15)
            logger.warning("Start date is in May, so adding 15 days to end date: %s", e_date.strftime("%Y-%m-%d"))

        # ===========================================================================

        start_date = s_date.strftime("%Y-%m-%d")
        end_date = e_date.strftime("%Y-%m-%d")

        sql = '''
            INSERT INTO tasks (task_name, task_description, task_assignee, task_start_date, task_end_date)
            VALUES("{:s}", "{:s}", {:d}, "{:s}", "{:s}")
        '''.format(name, description, user_id, start_date, end_date)

        c = self.connect_db().cursor()
        try:
            c.executescript(sql)
            message = "Successfully added task: %s"
            logger.info(message, name)
            return {"message": message.format(name)}, 201

        except sqlite3.IntegrityError as e:
            logger.error("DB integrity error: %s", e)
            return e, 400

    def get_task_by_id(self, task_id):
        sql = '''
            SELECT * FROM tasks WHERE task_id = {:d};
        '''.format(task_id)

        c = self.connect_db().cursor()
        c.execute(sql)
        task = c.fetchone()
        logger.info("Successfully got task info by id %s", task_id)

        return task

    def update_task(self, **kwargs):
        sql = '''
            UPDATE tasks SET
                task_name = "{:s}",
                task_description = "{:s}",
                task_assignee = "{:s}"
            WHERE
                task_id = {:d}
        '''.format(kwargs['task_name'], kwargs['task_descripiton'], kwargs['task_assignee'], kwargs['task_id'])

        c = self.connect_db().cursor()

        try:
            c.executescript(sql)
            logger.info("Successfully updated task {:s}", kwargs['task_name'])
            return True
        except sqlite3.IntegrityError as e:
            logger.error("Integrity error updating task id {:d}, name {:s}", kwargs['task_id'], kwargs['task_name'])
            return False

    def delete_task(self, task_id):
        sql = '''
            DELETE FROM tasks WHERE task_id = {:d};
        '''.format(task_id)

        c = self.connect_db().cursor()
        try:
            c.executescript(sql)
            logger.info("Successfully deleted task %s", task_id)
            return True
        except sqlite3.IntegrityError as e:
            logger.error("Error deleting task %s. Message: %s", task_id, e)
            return False

    # Helper  method to user id by name
    def __get_user_id(self, user_name):

        sql = '''
            SELECT user_id FROM users WHERE user_name="{:s}"
        '''.format(user_name)

        c = self.connect_db().cursor()
        user_id = c.execute(sql).fetchone()
        if user_id is None:
            return False

        return user_id[0]

    # Remove all tables
    def recreate_db(self):
        sql = '''
            DROP TABLE IF EXISTS tasks;
            DROP TABLE IF EXISTS users;
        '''
        c = self.connect_db().cursor()

        c.executescript(sql)

        logger.info("Deleted all tables")
        self.create_db_struct()

    # Get all tasks in DB
    def get_all_tasks(self):
        sql = '''
            SELECT task_id, task_name, task_description, task_start_date, task_end_date, user_name FROM tasks, users
            WHERE task_assignee = user_id;
        '''

        conn = self.connect_db()

        c = conn.cursor()
        c.execute(sql)

        tasks = c.fetchall()
        return tasks

    def get_all_users(self):
        sql = '''
            SELECT * FROM users;
        '''

        conn = self.connect_db()

        c = conn.cursor()
        c.execute(sql)

        users = c.fetchall()

        return users
