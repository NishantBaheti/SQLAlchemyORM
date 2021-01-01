from DBEngine import engine
from DBModelSqlite import Employee, Base
from sqlalchemy.orm import sessionmaker


class DBObj:
    def __init__(self):
        self.session = sessionmaker(bind=engine)

    def insertEmployee(self):
        pass

    def getAllEmployees(self):
        pass
