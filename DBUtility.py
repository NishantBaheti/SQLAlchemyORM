from DBEngine import engine
from DBModelSqlite import DeviceData, Base
from sqlalchemy.orm import sessionmaker


class DBObj:
    def __init__(self):
        self.engine = engine
        self.Session = sessionmaker(bind=self.engine)

    def insertDeviceData(self,timestamp,tagname,value):
        session = self.Session()
        try:
            data = DeviceData(
                timestamp=timestamp,
                tagname=tagname,
                value=value
                )
            session.add(data)
            session.commit()
            return True
        except Exception as e:
            print(str(e))
            return False
        finally:
            session.close()

    def getAllDeviceData(self):
        session = self.Session()
        try:
            data = session.query(DeviceData).all()
            return data
        except Exception as e:
            print(str(e))
            return None
        finally:
            session.close()

    def getDeviceDataforTag(self,tagname):
        session = self.Session()
        try:
            data = session.query(DeviceData)\
                .filter(DeviceData.tagname == tagname)\
                .all()
            return data 
        except Exception as e:
            print(str(e))
            return None
        finally:
            session.close()

    def getDeviceDataForId(self,idList):
        session = self.Session()
        try:
            data = session.query(DeviceData)\
                .filter(DeviceData.id.in_(idList))\
                .all()
            return data
        except Exception as e:
            print(str(e))
            return None
        finally:
            session.close()
