import time
import random

num=random.randint(1000,9999)#获取1000-9999之间的随机整数

numstr=str(num)  #数字转换成字符串 用str
time.sleep(1)  #延迟函数，延迟1秒

a=3.12645
print(round(a,2)) #保留下数点后2位小数，  得到值 3.13  round默认只取整数 如round(5.1) 得到5

#求最大值
max([1,3,4,56,7])  #得到值 56

b=input("请输入内容")  #用户输入内容

c="Hello"
d="World"
print(c,d)#得到  Hello World  中间多了一个空格
print(c+d)#得到   HelloWorld