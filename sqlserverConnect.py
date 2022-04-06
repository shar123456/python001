
import pymssql
 
# server    数据库服务器名称或IP
# user      用户名
# password  密码
# database  数据库名称
 






server = "DESKTOP-1A578AN\MSSQLSERVER2016"
user = "sa"
password = "sa123456"
database = "PythonDb"
conn = pymssql.connect(server, user, password, database)
if conn:
    print("连接成功!")

cursor = conn.cursor()









def CreateTable():
    sql = """
    IF OBJECT_ID('persons', 'U') IS NOT NULL DROP TABLE persons
    CREATE TABLE persons (id INT NOT NULL identity(1,1),name VARCHAR(100),age int,PRIMARY KEY(id))
    """
    cursor.execute(sql)
    conn.commit()

# 批量插入数据
 
 
def InsertData():
    sql = "INSERT INTO persons(name,age) VALUES (%s, %d)"
    data = [
        ('zhangsan', 15),
        ('lisi', 16),
        ('wangwu T.', 17)]
    cursor.executemany(sql, data)
    # 如果没有指定autocommit属性为True的话就需要调用commit()方法
    conn.commit()
 
# 删除操作
 
 
def DeleteData():
    sql = "delete persons where id=5"
    cursor.execute(sql)
    conn.commit()
 
# 查询操作
 
 
def SelectTable():
    sql = "SELECT * FROM persons"
    cursor.execute(sql)
    row = cursor.fetchone()
    while row:
        print("ID=%d, Name=%s" % (row[0], row[1]))
        row = cursor.fetchone()
    # 也可以使用for循环来迭代查询结果
    # for row in cursor:
    #     print("ID=%d, Name=%s" % (row[0], row[1]))
 
# 修改操作
 
 
def UpdateData():
    sql = "update [persons] set name ='Python1' where id<3"
    cursor.execute(sql)
    conn.commit()

#CreateTable()
#InsertData()
UpdateData()
SelectTable()
cursor.close()
conn.close()


