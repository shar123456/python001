#函数是组织好的，可重复使用的，用来实现单一或相关功能的代码段。
#函数能提高应用的模块性和代码的重复利用率。
def testFunc(name):   #定义一个函数
    print("正在执行函数:",name)
    return "返回结果"
getResult=testFunc("Hello")  #调用函数

def showInfo(name,age=12,hobby="暂无"): #age是默认参数 默认参数要放最后
    print("姓名:",name,"年龄:",age,"爱好:",hobby)

showInfo("king",hobby="踢足球") 
showInfo("star",15,hobby="打篮球") #关键词传参

#不定长参数示例
def add(*args):
    sum=0
    print(args) #不定长参数在函数中得到的是元组
    for i in args:
        sum+=i
    return sum

print(add(1,2,5,6))


