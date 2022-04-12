import numpy as np
'''
1.创建一个数组
.通过numpy array函数。从python lis土中创建数组
2.通过numpy zeros函数。创建全0数组
3.通过numpy ones图数，”创建全1数组
4。远过numpy eye困数，创建单位数组
5.通过numpy arange图数。创建等间隔的数字数组
6,迪过numpy random函数，创建随机数组
'''
#通过numpy array函数
#创建一个列表
array_list_1=[1,2,3,4,5]
array_list_2=[6,7,8,9,10]
#通过array函数创建一个数组
Arr1=np.array(array_list_1)
print(type(Arr1))
print(Arr1)
Arr2=np.array([array_list_1,array_list_2])
print(type(Arr2))
print(Arr2)

#通过numpy zeros函数
Arr3=np.zeros(shape=(3,4))#创建一个3行4列的全0数组
print(Arr3)


#通过numpy ones图数，”创建全1数组
Arr4=np.ones(shape=(3,4))#创建一个3行4列的全1数组
print(Arr4)

#远过numpy eye困数，创建单位数组
Arr5=np.eye(3)
Arr6=np.eye(3,4)
print(Arr5)
print(Arr6)

#通过numpy arange图数。创建等间隔的数字数组
Arr7=np.arange(1,10)#创建一个1-9的数组
Arr8=np.arange(1,10,0.5)#创建一个1-9的数组，间隔是0.5

#迪过numpy random函数，创建随机数组
#numpy random
#np.random.random ( 10)
#返回10个0-1之间的数据0,1)
#np.random.randn (10)返回10个服从标准正态分布的数据np.random.randint(10)返回0-9之间任意整数


'''
查看数组对象的属性
ndim 查看数组维度(一维、二维..--)
shape ,查看数组的大小
size，查看数组元素的总数
dtype ，查看数组中的数据类型，如果数组中都是整型，只有一个浮点类型，那么得到的是浮点类型
'''

list1=[1,2,3,4,5]
list2=[1,2,3,4,5]
arrTemp=np.array([list1,list2])
print(arrTemp.ndim)
print(arrTemp.shape)
print(arrTemp.size)
print(arrTemp.dtype)

#访问数组
print(arrTemp[0])#访问第0行
print(arrTemp[0][1])#访问第0行,第1列
print(arrTemp[0,1])#访问第0行,第1列

#特殊访问数组
arrTemp1=np.array([[1,2,3],[4,5,6],[7,8,9]])
#如果想获取到5689，如下：
print(arrTemp1[1:,1:])

#补充   reshape  可以将数组维度进行转换
#比如一维数组，转换成3行3列
arrTemp2=np.arange(1,10).reshape(3,3)
print(arrTemp2)