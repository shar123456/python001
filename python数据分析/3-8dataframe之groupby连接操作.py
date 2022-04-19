import pandas as  pd
import numpy as np
#groupby可以理解为,按照哪些字段进行分组
#以company为分组
#会返回一个DataFrameGroupBy对象

df1 = pd.DataFrame({'company': [ 'A', 'B' , 'A','C' ],
'age':[11, 21,23,53],
'salary':[1000,2000,1000,500]})
print(df1)




#可以通过list查看DataFrameGroupBy对象内部情况
# company通过groupby -- > A,B, c
#总结来说，groupby的过程就是将原有的DataFrame按照groupby的字段(这里是company)，划分为若干个分组DataFrame
g=df1.groupby('company')
print(list(g))
for t in list(g):
    print(t)


#通过get_group()方法，我们可以查看—个组的数据情况
print(g.get_group("A"))


#通过groupby分组后，可以通过agg函数，进行聚合操作
#min
#最小值
#max
#最大值
#sum
#求和
#mean
#均值
#median中位数
#count计数
#nunique 计算去重后个数(类似sQL count distinct)
#计算不同公司员工的平均年龄和平均薪水
print(g.agg("mean"))



#指定列。进行操作
#计算不同公司员工的平均年龄以及薪水的中位数
print(g.agg({'age':"mean",'salary':"sum"}))


#计算不同公司员工的平均年龄以及薪水的中位数，均值，总人数
print(g.agg({'age':"mean",'salary':["sum","median","count"]}))



#扩展
#count 计数, count不包含NaN值
#size 计数时包含NaN值
#nunique 计算去重后个数(类似sQL count distinct)

df = pd.DataFrame({"Name":["Alice","Bob","Mallory","Mallory","Bob","Mallory"],
"city" : [ "seattle", "seattle", "Portland","seattle" ,"seattle","Portland"],
"val":[4,3,3,np.NaN,np.NaN,4]})
print(df)

print(df.groupby ('city').agg({'val': [ 'count' , 'size' ]}))

print(df.groupby ('city').agg({'val': [ 'count' , 'size' ],'Name':'nunique'}))