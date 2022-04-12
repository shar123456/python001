import numpy as np
a=np.random.random(7) #创建7个0到1之间的数
print(a)
print(type(a))

#返回数组中最小值对应的索引
print(np.argmin(a))
#返回数组中最大值对应的索引
print(np.argmax(a))


# shuffle打乱数组的排序
x=np.arange(16).reshape(4,4)
np.random.shuffle(x)
print(x)


#sort排序
print(np.sort(x))
print(np.sort(x,axis=0))

#索引取值
print(x[0,[True,False,False,True]])#True代表0行  要访问的值，False代表不要访问

#筛选数组中大于等于3小于10的数值
print(x[(x>=3) &(x<10)])
#筛选数组可以整除2的数值
print(x[(x%2==0)])
