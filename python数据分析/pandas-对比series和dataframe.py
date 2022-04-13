'''
#简单来说,DataErame是多个共用相同索引的series组成#series没有列索引，DataFrame有列索引

'''
import pandas as pd

data = {
"name":['lemon', 'Jack','Jason' ], 
"age":[20,25,27],
"sex": ['male','female', 'male']
}
df=pd.DataFrame(data)
print(df)

#1.DataFrame可拆分成多个Series
print(df["name"])

#2.多个Series，也可组合成 DataFrame
name=df["name"]
age=df["age"]
print(pd.DataFrame([name,age]))
print(pd.DataFrame([name,age]).T)#倒转
print("#################")
#其他操作，逐行读取数值
for index,value in df.iterrows():
    print(index,value,sep="-----------------")
    name,age,sex=value#取值
    print(name)