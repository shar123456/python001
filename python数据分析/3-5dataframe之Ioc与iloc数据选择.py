
import pandas as pd
'''
loc

loc[ row,column]
row选择指定行数索引
df.loc[:,:],返回所有数据
df.loc[:3,:],返回前4行( 0,1,2,3)
column选择指的列名
df.loc[ :,"Stockcode"]返回series
df.loc[ :,["stockcode"]返回DataFrame

'''
df=pd.read_excel('../files/test1.xlsx',engine='openpyxl')
print(df.head())
print(df.loc[:,:])#返回所有数据
print(df.loc[:2,:]) #返回前3行
print(df.loc[:,['Name']])


#筛选特定条件的DataFrame
# #选择Name为queen

print(df.loc[df.Name=="queen"])

#返回索引偶数行
print(df.loc[df.index%2==0])


'''
iloc   与loc的不同是 逗号后面不能输入列名
# df.iloc[ :3,:]返回前3行(o.1,2)  这个与loc有区别 loc是返回前4行(0,1,2,3)
# df.iloc[ :3,:3]返回前3行(0,1,2)。前3列(0,1,2)
'''

print(df.iloc[:,:])#返回所有数据
print(df.iloc[:3,:])#返回前3行(o.1,2) 