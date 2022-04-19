import pandas as pd
import numpy as np
'''
#pivot_table可理解为Excel中使用数据透视表

#当我们建立数据透视表时，我认为最简单的方法是一步一步地做。
# 添加项目并检查每个步骤，以验证你正在获得预期的结果。
# #创建—个最简单的数据透视表,一定需要有一个索引,即index
'''
df=pd.read_excel('../files/test1.xlsx',engine='openpyxl')
print(df.head())
#创建数据透视表
#以Name列为索引
tsb=df.pivot_table(index="Name")   #索引值为表中的某一列的名
print(tsb)

#以Name和Hobby列为索引
tsb1=df.pivot_table(index=["Name","Hobby"])   #索引值为表中的某一列的名
print(tsb1)

#指定value
tsb2=df.pivot_table(index=["Name","Hobby"],values=["Age"])   #索引值为表中的某一列的名
print(tsb2)

#更改value统计方式 默认是均值mean
# np.sum,len,np.mean
tsb3=df.pivot_table(index=["Name","Hobby"],values=["Age"],aggfunc=[np.sum,len])   #索引值为表中的某一列的名
print(tsb3)

##显示相关产品销售情况
# #columns

tsb4=df.pivot_table(index=["Name","Hobby"],values=["Age"],aggfunc=[np.sum],columns="Level")   #索引值为表中的某一列的名
print(tsb4)

##对缺失值(NaN),填充为0
# #fill_value
tsb5=df.pivot_table(index=["Name","Hobby"],values=["Age"],aggfunc=[np.sum],columns="Level",fill_value=0)   #索引值为表中的某一列的名
print(tsb5)

##添加行与列统计#margins
#统计方式,取决于aggfunc

tsb6=df.pivot_table(index=["Name","Hobby"],values=["Age"],aggfunc=[np.sum],columns="Level",fill_value=0,margins=True)   #索引值为表中的某一列的名
print(tsb6)

#扩展
#aggfunc可传入字典,指定列进行相关计算
tsb7=df.pivot_table(index=["Name","Hobby"],values=["Age","workYear"],aggfunc={"Age":np.sum,"workYear":np.mean},columns="Level",fill_value=0,margins=True)   #索引值为表中的某一列的名
print(tsb7)
