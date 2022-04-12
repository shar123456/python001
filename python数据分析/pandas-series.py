import numpy as np
import pandas as pd
#pandas有两种主要的数据结构，Series和DataFrame

#1.什么是Series 可以理解为 1维数组数值+索引 组成

#如何创建Serise  有三种方式

#1.通过Array方式创建Series
arr_1=np.array(['a','b','c'])
s1=pd.Series(arr_1)
print(s1,type(s1))

#2.通过列表的方式创建Series
list_2=[1,2,3,4,5]
s2=pd.Series(list_2)
print(s2,type(s2))


#3.通过字典的方式创建Series,注意的是通过字典的方式创建Series 它的键就是它的索引
dic_1={'a':1,'b':2,'c':3}
s3=pd.Series(dic_1)
print(s3,type(s3))

#Series的相关操作
#1. 指定索引,指定索引要确保长度和值是一样的，否则会报错

arrTemp=np.array([1,2,3,4,5])
sTemp=pd.Series(arrTemp,index=['a','b','c','d','e'])  #将默认的索引值 012345 替换成abcde,
print(sTemp,type(sTemp))

#2.获取Series的索引 和值
print(sTemp.index,type(sTemp.index),sTemp.values,type(sTemp.values))


#3.Series的运算  加减乘除操作
print(sTemp+1)  #相应位都会+1
print(sTemp-1)
print(sTemp*2)
print(sTemp/2)

#4.筛选出大于3的值，和操作数组的方式差不多
print(sTemp[sTemp>3])
#5.取它的值
print(sTemp[sTemp>3].values,type(sTemp[sTemp>3].values))

#6.Series之间的操作
#对应的index位置操作
#若无相同的索引，那么最终结果会赋值为NaN
SerA=pd.Series([1,2,3],index=['a','b','c'])
SerB=pd.Series([1,2,3],index=['b','c','d'])
print(SerA+SerB)
