import os

from petisco import ApplicationConfigurer, databases
from petisco.extra.sqlalchemy import MySqlConnection, SqlDatabase, SqliteConnection

DATABASE_NAME = "sql-tasks"
ROOT_PATH = os.path.abspath(os.path.dirname(__file__))
SQL_SERVER = os.getenv("SQL_SERVER", "sqlite")


class DatabasesConfigurer(ApplicationConfigurer):
    def execute(self, testing: bool = True) -> None:
        if testing or (SQL_SERVER == "sqlite"):
            test_db_filename = "tasks.db"
            connection = SqliteConnection.create("sqlite", test_db_filename)
        else:
            connection = MySqlConnection.from_environ()

        sql_database = SqlDatabase(alias=DATABASE_NAME, connection=connection)

        databases.add(sql_database)
        databases.initialize()


configurers = [DatabasesConfigurer()]
