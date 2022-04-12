import numpy as np


#单一维度的聚合
arr=np.arange(9)
print(np.sum(arr)) #求数组中的和
print(np.max(arr)) #求数组中的最大值
print(np.min(arr)) #求数组中的最小值

#多维度的聚合
#axis=0 沿着横轴方向压缩 看纵轴   1沿着纵轴方向 看横轴
arr2=np.arange(16).reshape(4,4)
print(arr2)
print(np.sum(arr2,axis=0)) #求数组中的和
print(np.sum(arr2,axis=1)) #求数组中的和
print(np.min(arr2,axis=1)) #求数组中的和


print(np.mean(arr2,axis=1)) #求数组中的均值


#percentile分位数
#np.random.rand(100000) 返回1000000个0-1之间的数据
a=np.random.rand(100000)
print(np.percentile(a,q=25))