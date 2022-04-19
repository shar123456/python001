import pandas as pd
import numpy as np

#rename修改列名与索引

data={'company': ['B','A','B','B'],
'gender': ['female', 'female' ,'male','male'],
'num':[40,32,35,12]
}
df=pd.DataFrame(data)
print(df)

#将列名num -- age
#将索引0-3 -- A-D
df=df.rename(columns={'num':'age'})
print(df)
df=df.rename(columns={'num':'age'},index={0:"A",1:"B",2:"C",3:"D",})
print(df)

#如果希望直接生效，加inplace=True参数,这样就不用重新在赋值了
df.rename(columns={'num':'age'},index={"D":"F"},inplace=True)
print(df)


#set_ index
#将DataFrame中的某一(多) 个字段设置为索引
df.set_index(['company'],inplace=True)
print(df)

# reset_index
#重置索引
# drop=True删除原索引
# drop=False保留原索引，并作为DataFrame新字段
df.reset_index(drop=True,inplace=True)
print(df)



#drop duplicates 如果不传参数 会将所有字段一样的重复列去除，如果指定字段，则会去除该字段的重复
#去除重复值
#subset可指定列作为主键
# keep first/last, 默认first  first是指去除后保留第一行，last是指去除后保留最后一行
#df.drop_duplicates(subset=['gender'],inplace=True)
df.drop_duplicates(subset=['gender'],keep="last",inplace=True)
print(df)

#drop
#可删除DataFrame指定列与索引
#df.drop(columns="age",index=0,inplace=True)

#isin
#常用于构建布尔索引对DataFrame的数据进行条件筛选
#比如筛选都为male的数据
#df.loc[df.gender.isin(['male'])]



