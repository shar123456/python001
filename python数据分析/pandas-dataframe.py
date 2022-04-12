import numpy as np
import pandas as pd

'''
1.什么是DataFrame
DataFrame是一个表格型的数据结构，它含有一组有序的列，每列可以是不同的值类型(数值、字符串、布尔值等)。
2DataFrame既有行索引也有列索引，它可以被看做由series组成的字典(共用同一个索引)
3可以理解成一个表

'''

#如何创建DataFrame

#1.通过数组的方式
arr=np.array([[1,2,3],[4,5,6]])
df=pd.DataFrame(arr)
print(df,type(df),sep='\t\t')
df1=pd.DataFrame(arr,columns=['a','b','c']) #指定列索引
df2=pd.DataFrame(arr,index=['d','e']) #指定行索引
print(df1,df2,sep='\n')


#通过字典的方式创建DataFrame
df_dict = {'state':{0: 'ohio',1: 'ohio', 2: 'ohio',3: 'mevada' ,4: 'Revada ' },
'year' : {0: 2000,1: 2001,2: 2002, 3: 2001, 4: 2002},
'pop':{0: 1.5, 1: 1.7,2: 3.6,3: 2.4, 4: 2.93}}
df3=pd.DataFrame(df_dict)
print(df3)


#DataFrame常见的操作
#1.head查看头数据  tail查看尾数据
print(df3.head(3))  #查看前3行的数据
print(df3.tail(2))  #查看后2行的数据
#2.通过info查看数据结构和存储信息
print(df3.info())

#3.describe 查看数据按列的统计信息
print(df3.describe())

#4.返回每一列的均值和中位数
print(df3.mean())
print(df3.median())

#5.index 获取行索引
print(df3.index)
#6.columns获取列索引
print(df3.columns)

#7. 转置 index 与columns对调
print(df3.T)

#8.排序
# sort_index
#0-- index
#1---column
#sort_value
print(df3.sort_index(axis=0,ascending=False))  #第二个参数是行索引按照降序排列，第一个是按照行索引排