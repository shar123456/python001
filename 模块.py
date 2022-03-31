#模块是python中的最高级别组织单元，它将程序代码和数据封装起来以便重用
#模块的作用 ：代码重用   实现共享服务和数据
#模块包括 自定义模块  内置模块 已经第三方模块

#导入内置模块 生成随机数的模块
import random   #导入内置模块 random  生成随机数的模块
print(random.random())  #生成0-1之间的小数
print(random.choice(["star","king","queen"]))  #在给定的列表中随机生成一个名字
print(random.randint(1,10))  #生成1-10之间随机的整数
#如果只想引入random的choic方法，如下：
#from random  import choice
#from random  import choice,random
#from random  import *  从random模块中引入所有方法

#导入自定义模块
import MyLibs.testPackage   
MyLibs.testPackage.mytestFunc() #执行自定义模块中的方法


#导入内置的爬虫模块
from urllib import request
url="http://www.baidu.com"
datas=request.urlopen(url).read()
#print(datas.decode())

#导入内置的系统模块
import os
#os.rename(r"F:\aaa.docx",r"F:\bbb.docx") #将aaa文档的名字改成bbb  对文件重命名

#导入内置的控制浏览器的模块
import webbrowser
#webbrowser.open("http://www.baidu.com")  #打开浏览器的百度页面

#安装第三方模块
#下载第三方模块 可以使用pip  这个是按照python的时候 自带的包管理工具
#第一次使用pip 要先升级 在命令行窗口中执行命令 命令如: python -m pip install --upgrade pip
#安装第三方图片处理模块  pip install pillow  卸载pip uninstall pillow
#pip list 查看已经安装的第三方包
from PIL import Image,ImageFilter

#打开一个jpg图像文件
im=Image.open(r'F:\python\python初学者教程\pycode\python001\images\bg1.jpg')
#应用模糊滤镜器
im2=im.filter(ImageFilter.BLUR)
im2.save(r'F:\python\python初学者教程\pycode\python001\images\bg2.jpg')