#定义一个类
class Dog(object):#object是一个类，Dog继承这个类，当然也可以继承其他的类

	TypeDog="宠物"#定义一个属性，这个属性叫类属性，下面init方法中定义的属性叫做实例属性
	
	def __init__(self,name,age,color):
		self.name=name
		self.age =age
		self.color=color 		  
    

	def eat(self):#定义一个普通方法，方法中的self是必须要加的，是规定
		print("狗吃骨头")

	def run(self,speed,remark="暂无备注"):
		print(self.name,"正在奔跑,速度是：",speed,"特性：",remark)#self.name 是拿到了当前对象的name属性的值

#实例化对象
dog=Dog("小黑",20,"白色")
dog.color="绿色"#修改实例属性
print(dog.name)
print(dog.color)
dog.eat()#调用方法
dog.run("3m/s")#调用方法,并给方法传递参数
dog.run("3m/s","很可爱！")#调用方法,并给方法传递参数