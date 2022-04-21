import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

x_data =[2011,2012,2013,2014,2015,2016,2017]
y_data=[58000,60200,63000,71000,84000,90500,107000]
y_data2 =[52000,54200,51500,58300,56800,59500,62700]
y_data3 =[12000,2420,21500,18300,3450,3400,56700]
#简单绘制
plt.plot(x_data,y_data)
plt.plot(x_data,y_data2)
#plt.show()  #如果不加show会出现 [<matplotlib.lines.Line2D object at 0x000001F630DBD2C8>] 因为在一些软件不需要输入show（）就可以显示，但是在有些软件是不可以的。建议一定添加~


#指定折线颇色color,#linewidth#指定折线宽度
#linestyle_指定折线的样式
# -代表实线  默认
#--代表虚线
#-.代表短线、点相间的虚线
#:代表点线

#label 指定标签说明
#需plt.legend


#xlabel添加x轴描述
#ylabel添加y轴描述
#title 添加标题

#axis
#设置坐标轴范围 #plt.axis ([x_min, x_max,y_min, y_mOX])

#grid添加网格
#axis="x"在x轴添加网格  axis= "y"在y轴添加网格

plt.plot(x_data,y_data3,color="yellow",linewidth=3,linestyle="--",label="y_data3")
plt.xlabel("year")
plt.ylabel("sales")
plt.title("sales datas")
plt.axis([2010, 2020,100, 130000])
plt.legend()
plt.grid()#plt.grid(axis="x") 加参数 只会在横轴上显示网格
plt.show() 