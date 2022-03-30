#定义一个Animals类
class Animals(object):#该类继承与object类
      
       def __init__(self,color):
      	 self.color=color
       def eat(self):
       	   print("动物在吃草！")
       def run(self):
           print("动物在奔跑！")

class Dog(Animals):#定义一个Dog类继承Animals类
      def __init__(self,name,age):
      	self.name=name
      	self.age=age
      def eat(self):
      	print("狗喜欢吃肉！")

class Deer(Animals):#定义一个Deer类继承Animals类
      def __init__(self,name,age,color):
      	super(Deer,self).__init__(color)#调用父类的初始化方法
      	self.name=name
      	self.age=age
      def eat(self):
      	print("l鹿是草是动物！")


dog=Dog("大黄",20)  #print(dog.color)这种情况下，调用color属性会报错
dog.eat()
dog.run()

deer=Deer("小鹿",21,"白色")
print(deer.color)#这种情况下可以调用color属性
deer.eat()



#多态
def feed(obj):
	obj.eat()
an=Animals("紫色")
an2=Dog("二黄",22)
an3=Deer("美丽",23,"绿色")
feed(an2)


