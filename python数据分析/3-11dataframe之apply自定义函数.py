import pandas as pd
import numpy as np

#apply 是 pandas 库的一个很重要的函数，可以直接用于DataFrame和 series 对象。
#apply主要用于数据聚合运算，和自定义函数的运算

df1 = pd.DataFrame(
{
'name': [ "Star", "King" , "Queen" ],
'nation':["汉族", "满族","回族"],
'score':[123,345,223],
'date_from':["2019-04-01","2019-05-20","2019-05-01"],
'date_to':["2019-04-10","2019-05-25","2019-05-16"],
}
)

print(df1.head())

#数据聚合运算
# 对score 开根号
# np.sqrt
print(df1.score.apply(np.sqrt))

#如果民族不是汉族，则总分在考试分数上再加10分
df1['other_score'] =df1.nation.apply(lambda x: 0 if x =='汉族' else 10)
print(df1)
df1['total_score'] =df1.score+df1.other_score
print(df1)

#计算时间间隔
#apply(pd.to_datetime)  将字符串转换为python的时间格式
#x.days 
diff=df1.date_to.apply(pd.to_datetime)-df1.date_from.apply(pd.to_datetime)
print(diff)
df1["interval"]=df1.date_to.apply(pd.to_datetime)-df1.date_from.apply(pd.to_datetime)
print(df1)

#去掉days
df1["intervalNodays"]=df1.interval.apply(lambda x:x.days)
print(df1)


# score >600且interval<=15
#打个标签--> 1,否则为0
#涉及多列的时候，建议采用自定义函数的方式
#涉及多列的时候，axis = 1  这个参数不传会报错



def f(x):
    if x.score >= 600 and x.interval <=15:
        return 1
    return 0
df1["labels"]=df1.apply(lambda x : f(x),axis = 1)
print(df1)