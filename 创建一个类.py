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



#类的封装
class Card(object):
	def __init__(self,num,pwd,ban):
		self.num=num
		self.__pwd=pwd  #密码  加两个下划线变成私有属性(只能在类的内部被访问)
		self.ban=ban 
	
	def __saveMoney(self):  #方法加两个下划线 变成私有方法，只能在类内部使用
		pass
	def getMoney(self,sum):  
		self.ban-=sum
		print("父类取钱")
		return self.ban

	def getBan(self,numTemp,pwdTemp):
		if self.num==numTemp and self.__pwd==pwdTemp:
			return self.ban
		else:
			print("密码错误，禁止访问.")

card=Card("1001","123456",1000)  #开卡

#如果想强制取私有属性，可以通过下面方式
print(card._Card__pwd)



#类的继承
class JHCard(Card):
	pass
card1=JHCard("1001","123456",1000)  #开卡
print(card1.getBan("1001","123456"))


#类中方法的重写
class GHCard(Card):
	level="0级别"

	def __init__(self, num, pwd, ban,level):
		self.level=level
		super(GHCard,self).__init__(num, pwd, ban)  #调用父类的构造函数
	def getMoney(self,sum): #如果子类中定义的方法和父类中一样，那么会优先执行子类中的方法
		self.ban-=sum
		print("您的余额为:",self.ban,"取款金额为:",sum,"当前vip等级为:",self.level)
	
card2=GHCard("1001","123456",1000,"1级")  #开卡
card2.getMoney(90)