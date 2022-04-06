import datetime

#获取当前日期
dateNow=datetime.datetime.now()
print(dateNow)

#获取一个指定的日期
d=datetime.datetime(2022,10,1,12,34,45)
print(d)

#日期和字符串之间的相互转换
dstr=d.strftime("%Y-%m-%d %H:%M:%S")
print(dstr)

#字符串转日期
stime="2022-8-15 3:34:45"
dateTime=datetime.datetime.strptime(stime,"%Y-%m-%d %H:%M:%S")
print(dateTime)