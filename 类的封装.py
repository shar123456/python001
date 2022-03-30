class Card(object):
	
	def __init__(self, num,pwd,ban):
		self.num = num#卡号
		self.pwd = pwd#密码
		self.__ban = ban#余额  双下划线代表私有属性，只能在类部被访问，也可以在方法的名字前加双下划线，变成私有方法，只能在内部访问。

	def getban(self):#如果想要从对象的外部获取私有属性的值，那么可以通过此间接的方式
		return self.__ban 

	def cun(self):
		print("存款！")



card=Card("1001","123456","1000")#开卡
print(card.num)
print(card.getban())
print(card._Card__ban)#注意私有属性虽然只能在类的内部被访问，但是可以通过这个特殊的方式直接在外部访问。