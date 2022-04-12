
import numpy as np
a=np.arange(1,10).reshape(3,3)
b=np.arange(1,10).reshape(3,3)
print(a)
print(b)

#相加和相减，乘法，相除，是对应位置的相加或相减，乘法，相除操作，  两个数组必须满足行列相同
print("数组的加法",a+b)
print("数组的减法",a-b)
print("数组的乘法",a*b)
print("数组的除法",a/b)


#矩阵之间运算
#矩阵只能是二维,数组可以是多个维度,矩阵是数组的子集

#创建一个数组
arr1=np.array([[1,2,3],[4,5,6],[7,8,9]])
#将数组转换成矩阵
matrix_A=np.matrix(arr1)
matrix_B=np.matrix(arr1)
print("matrix_A",matrix_A)
print("matrix_B",matrix_B)
#矩阵的加法和减法  对应位置相加或相减
print("matrix_A+matrix_B",matrix_A+matrix_B)


#矩阵的乘法，必须满足矩阵c的列数必须能与d的行数,否则会报错
c=np.matrix(np.arange(12).reshape(3,4))
d=np.matrix(np.arange(12).reshape(4,3))
print("matrix_c*matrix_d",c.dot(d))