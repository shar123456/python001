
from DbCore.sqlServerOrm import *

class Person(object):
    db=None
    def __init__(self):
        self.db=PyDbContext()

    #查询所有用户
    def getAllPersons(self):   
        personsList=self.db.getDatas("SELECT * FROM persons")
        print("Id\t\tName\t\tAge")
        for person in personsList:
            for p in person:
                print(p,end="\t\t")
            print()
        

    #根据Id查询用户
    def getPersonsById(self):
        id=input("请输入用户Id:")
        sql='SELECT * FROM persons where id='+id      
        person=self.db.getDatas(sql)
        if person!=None and len(person)>0:
            for p in person[0]:
                print(p,end="\t\t")   
            print()  
        else:
            print("未查找到该用户.")   

    #增加用户
    def addPerson(self):
        name=input("请输入姓名:")
        age=str(input("请输入年龄:"))
        sql="insert into persons(name,age) values"
        sql+="('"+name+"',"+age+")"
        #print(sql)
        self.db.InsertDatas(sql)
    
    def closeConn(self):
        self.db.CloseConn()
