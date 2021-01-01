from sqlalchemy import create_engine
from DBModelSqlite import Base as SqliteBase
from DBModelMysql import Base as MysqlBase
from Config import DATABASE_PATH, APP_NAME


# SQLITE
engine = create_engine(f"sqlite:///{DATABASE_PATH}", echo=True)
SqliteBase.metadata.create_all(engine)


"""
start mysql server using docker 
- docker pull mysql:latest
- docker run -p 3000:3306 -p 33060:33060 --name mysql -e MYSQL_ROOT_PASSWORD=<some-password> -d mysql:latest
- docker container logs mysql 
"""


# mysql sql server
# engine = create_engine(
#     f"mysql+pymysql://root:<some-password>@localhost:3000/{APP_NAME}")
# MysqlBase.metadata.create_all(engine)
