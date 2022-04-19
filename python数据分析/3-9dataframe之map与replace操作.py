import pandas as  pd
import numpy as np

#Map 的操作对象是Series
df1 = pd.DataFrame(
{
'height': [ 178, 158 , 169,180,185 ],
'weight':[11, 21,23,53,43],
'smoker':[False,True,False,True,True],
'gender':["-","男","男","男","女"],
'age':[89,12,132,12,26],
'color':["black","yellow","black","black","red"],
}
)

print(df1.head())
#如果想将gender中
#男-->0
#女-->1
#map
#arg
#dict根据字典的键值对，替换series里面的值。
#若字典中，没有栈到series中对应的值，则赋值为NaN
#na_action
#如果传入ignore ,列跳过对空值的操作
print(type(df1.gender))
print(df1.gender.map({"男":1,"女":0}))

s=pd.Series(["cat","dog",np.nan,"pig"])
print(s.map("i am a {}".format))
#na_action
#如果传入ignore ,列跳过对空值的操作
print(s.map("i am a {}".format,na_action="ignore"))

#replace
#to_replace，若在series中存在的值即替换，series中不存在的值维持原状
# #inplace

df = pd.DataFrame (
{"名称":["产品1","产品2","产品3","产品4","产品5"],
"金额": [ 0,0.48,"F",0.74,0],
"合计":[0.37,0.28,"c",0.57,0.06],
}
)
#指定列替换  
print(df.金额.replace({"F":0}))
print(df)
print(df.金额.replace({"F":0},inplace=True))#inplace=True让替换生效
print(df)

#不指定列替换
print(df.replace({"c":2}))
