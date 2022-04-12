import pymssql

class PyDbContext(object):
    __server = "DESKTOP-1A578AN\MSSQLSERVER2016"
    __user = "sa"
    __password = "sa123456"
    __database = "PythonDb"
    __conn=None
    __cursor=None
    #建立链接
    def __init__(self):
        try:
            self.__conn = pymssql.connect(self.__server, self.__user, self.__password, self.__database)
            if self.__conn:         
                        self.__cursor = self.__conn.cursor()
                        print("连接成功.")
            else:
                  print("连接失败.")
        except Exception as e:
           print("连接失败,错误:",e)
          

    # 查询数据
    def getDatas(self,sql):
        try:
            self.__cursor.execute(sql)
            listTemp=[]
            for row in self.__cursor.fetchall():
                #print(row)
                listTemp.append(list(row))
            return listTemp
        except Exception as e:
           print("出现错误,错误:",e)
           # 关闭连接
           self.CloseConn()

        # 查询数据
    def InsertDatas(self,sql):
        try:
            self.__cursor.execute(sql)
            self.__conn.commit()
            print('成功写入', self.__cursor.rowcount, '条数据')
        except Exception as e:
           print("出现错误,错误:",e)
           # 关闭连接
           self.CloseConn()

           # 删除数据
    def DeleteDatas(self,sql):
        try:
            self.__cursor.execute(sql)
            self.__conn.commit()
            print('成功删除', self.__cursor.rowcount, '条数据')
        except Exception as e:
           print("出现错误,错误:",e)
           # 关闭连接
           self.CloseConn()

                 # 更新数据
    def UpdateDatas(self,sql):
        try:
            effectRows=self.__cursor.execute(sql)
            self.__conn.commit()
            print('成功更新', effectRows, '条数据')
        except Exception as e:
           print("出现错误,错误:",e)
           # 关闭连接
           self.CloseConn()

               # 关闭连接
    def CloseConn(self):
        try:
            self.__cursor.close()
            self.__conn.close()
            print('连接已关闭.')
        except Exception as e:
           print("出现错误,错误:",e)
          
        
        

