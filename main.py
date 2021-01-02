from DBUtility import DBObj
from datetime import datetime 

dbObj = DBObj()

for i in range(100):
    dbObj.insertDeviceData(
        timestamp=datetime.now(),
        tagname="tag1",
        value=10.0000001+i
    )

for i in dbObj.getAllDeviceData():
    print(i.timestamp,i.tagname,i.value)

for i in dbObj.getDeviceDataforTag(tagname="tag1"):
    print(i.timestamp,i.tagname,i.value)

for i in dbObj.getDeviceDataForId([1,2,3,4,5,10]):
    print(i.id,i.timestamp,i.tagname,i.value)