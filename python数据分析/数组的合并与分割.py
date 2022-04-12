import numpy as np
#数组的合并 
#np.concatenate 连接数组
#axis=0  垂直方向堆叠数组
#axis=1  水平方向堆叠数组

a=np.arange(6).reshape(2,3)
b=np.arange(3).reshape(1,3)
c=np.arange(10).reshape(2,5)

print("a和b在垂直方向合并",np.concatenate([a,b],axis=0))
print("a和c在水平方向合并",np.concatenate([a,c],axis=1))


#np.vstack 在垂直方向堆叠数组，两个数组需要相同的列数
print(np.vstack([a,b]))
#np.hstack 在水平方向堆叠数组，两个数组需要相同的行数
print(np.hstack([a,c]))


#数组的分割
#np.split(）
#indices_or_sections
#1如果“索引或区段*是整数N,则数组将沿着“轴被分成N个相等的数组。如果N无法整除，则会引发一个错误
#2[2,5] 传数组的时候，比如这个，就是分3段，如下
#ary[:2]
#ary[2:5]
#ary[5:]
#axis分割的轴,axis 默认为0 水平方向，2 垂直方向

arr1=np.arange(9)
print(arr1)
print(np.split(arr1,3))
print(np.split(arr1,[2,5]))


arr2=np.arange(16).reshape(4,4)
print(np.split(arr2,2,axis=0))
print(np.split(arr2,2,axis=1))