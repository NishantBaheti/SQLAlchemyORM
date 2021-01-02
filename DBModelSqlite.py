from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, BigInteger, VARCHAR, DateTime, Integer

Base = declarative_base()


class DeviceData(Base):
    __tablename__ = "DeviceData"
    id = Column(BigInteger().with_variant(Integer, "sqlite"), primary_key=True)
    timestamp = Column(DateTime, nullable=False)
    tagname = Column(VARCHAR, nullable=False)
    value = Column(VARCHAR)


"""
Ref.-
https://docs.sqlalchemy.org/en/latest/dialects/sqlite.html#allowing-autoincrement-behavior-sqlalchemy-types-other-than-integer-integer
https://medium.com/@jorlugaqui/fixing-sqlalchemy-autoincrement-issue-for-sqlite-997300307bda
"""
