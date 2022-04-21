import pandas as pd
import numpy as np


data = {"company":[ "B", "A","B" , np.nan],
"gender":["female" , "female", "male" , "male"],"age": [40,31,28,28]}
df=pd.DataFrame(data)
print(df)

#value _counts
#统计分芙变量中每个类的数量  如果是数字类型的不行
# normalize返回各类的占比
print(df.gender.value_counts())
print(df.gender.value_counts(normalize=True))#返回各类占比

#isna
#判断DataFrame、Series 是否为缺失值。是的话返回True，否的话返回False
print(df.isna())
print(df.company.isna())
#直接返回有缺省值的一行
print(df.loc[df.company.isna()])

#any
#大多数情况下数据量较大,不可能直接isna后一个一个看是否是缺失值。
# any ()和isna()结合使用可以判断某—列是否有缺失值
#df.isna().any()
print(df.isna().any())

#dropna
#删掉含有缺失值的数据
print(df.dropna(inplace=True))

#filina
#填充缺失数据value
#或method
#pad /ffill  用上一个值填充
#backfill / bfill: 用下一个值填充

print(df.fillna(value=0))#将缺省值填充为0
#print(df.fillna(method='pad'))#将缺省用上一个填充 或这么写print(df.fillna(method='ffill'))

#sort_values
#按照某列进行排序《用by参数控制)，对series按数据列进行排序。
df.sort_values(by="age")  #默认是由小到大   从大到小 加参数 df.sort_values(by="age",ascending=False) 
