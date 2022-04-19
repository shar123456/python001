
import pandas as  pd
import numpy as np

#pd.cut常用来把一组数据分割成离散的区间
score = np.random.randint ( 25,100,size=10)#随机生成10个25到100之间的随机数

#pd.cut
#x:被切分的类数组(array / series)数据，必须是1维的;
# bins: bins是被切割后的区间
      #int :当bins为一个int型的标量时，，如bins = 3，代表将x分成3个区间。
      # sequence:指定区间[0,59,70,80,100]
print(pd.cut(score,bins=3))

#right: bool型参数，默认为True，表示是否包含区间右部。比如如果bins=[1,2,3 ],
# #right=True，则区间为(1,3],(2,3]
#right=False，则区间为[1,2),[2,3)。
print(pd.cut(score,bins=3,right=False))

print(pd.cut(score,bins=[0,59,70,80,100],right=False))


#labels:给分割后的bins打标签，比如把年龄x分割成年龄段bins后，可以给年龄段打上诸如青年、中年的标签。
# labels的长度必须和划分后的区间长度相等，比如bins=[1,2，3]，划分后有2个区间(1,2]，(2,3]，
# 则labels的长度必须为2。#【 'low ' , 'middle ", 'good', 'perfect "]
print(pd.cut(score,bins=[0,59,70,80,100],right=True,labels=['low', 'middle', 'good' , 'perfect']))


#更换为DataFrame查看数据
s= pd.DataFrame(score,columns=[ "score"])
print(s)
#label
s["range"] = pd.cut (s.score,bins=[0, 59,70,80,100])
print(s)

s1 = pd.cut (s.score,bins=[0, 59,70,80,100],labels=['low', 'middle', 'good' , 'perfect'])
print(s1)
s["label"] = pd.cut (s.score,bins=[0, 59,70,80,100],labels=['low', 'middle', 'good' , 'perfect'])
print(s)

#groupby查看数据统计
print(s.groupby("range").agg({'label': 'count'}))