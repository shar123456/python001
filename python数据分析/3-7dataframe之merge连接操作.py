import pandas as pd


df1 = pd.DataFrame({'lkey': [ 'foo', 'bar' , 'baz','lemon' ],
'value':[1, 2,3,5]})
df2 = pd.DataFrame({'rkey':['foo','bar', 'baz', 'jack' ],
'value':[ 5, 6,7,8]})
print(df1,df2,sep="\n")


#（一）inner join内连接
#根据on条件,列出左右两表共有的数据
dtInner=pd.merge(df1,df2,left_on='lkey',right_on='rkey' ,how ='inner' )
print("内连接",dtInner,sep="\n")
#通过suffixes可更改列的名
dtInner1=pd.merge(df1,df2,left_on='lkey',right_on='rkey' ,how ='inner',suffixes=('_lkey','_rkey') )
print("内连接suffixes",dtInner1,sep="\n")

#（二）left join左连接
#产生表1的完全集，而表2中匹配的则有值，没有匹配的则以NaN(null)值取代

dtLeft=pd.merge(df1,df2,left_on='lkey',right_on='rkey' ,how ='left' )
print("左连接",dtLeft,sep="\n")

#(三)right join_右连接
#产生表2的完全集，而表1中匹配的则有值，没有匹配的则以nul值取代
dtright=pd.merge(df1,df2,left_on='lkey',right_on='rkey' ,how ='right' )
print("右连接",dtright,sep="\n")

#(四)  outer  全连接  将两列的所有的值都返回
dtouter=pd.merge(df1,df2,left_on='lkey',right_on='rkey' ,how ='outer' )
print("全连接",dtouter,sep="\n")