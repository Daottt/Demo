import os.path
import sqlite3

class DataBaseManager:
    def __init__(self, base_path):
        self.base_path = base_path

        if not os.path.exists(self.base_path):
            connection = sqlite3.connect(self.base_path)
            connection.close()
            self._execute_file(r"src\database\base.sql")

    def _execute_file(self, sql_file):
        connection = sqlite3.connect(self.base_path)
        cur = connection.cursor()
        with open(sql_file, "r") as file:
            scripts = file.read()
            try:
                cur.executescript(scripts)
            except():
                print("error")
            finally:
                connection.close()

    def execute(self, query):
        connection = sqlite3.connect(self.base_path)
        cur = connection.cursor()
        res = cur.execute(query).fetchall()
        connection.commit()
        connection.close()
        return res

    def login(self, login: str, password: str):
        return self.execute(f"Select * From Users Where login = '{login}' AND password = '{password}'")

    def check_login(self, login: str):
        return self.execute(f"Select login From Users Where login = '{login}'")

    def get(self, table, e_id):
        return self.execute(f"Select * From {table} Where id = {e_id}")

    def get_all(self, table):
        return self.execute(f"Select * From {table}")

    def get_tasks(self):
        res = self.execute(f"Select Task.id, TaskStatus.*, master.*, client.* From Task "
                           f"Inner Join TaskStatus on TaskStatus.id = Task.status_id "
                           f"Inner Join TechType on TechType.id = Task.tech_type_id "
                           f"Inner Join Users as master on master.id = Task.master_id "
                           f"Inner Join Users as client on Task.client_id = client.id ")
        return res

    def create(self, table: str, values: dict):
        self.execute(f"Insert into {table} {tuple(values.keys())} values{tuple(values.values())}")

    def update(self, table: str, values: dict, index: int):
        self.execute(f"update {table} set {tuple(values.keys())} = {tuple(values.values())} "
                     f"Where id = {index}")

