class Person():
	def __init__(self):
		self.__money = 100#私有属性






	def getMoney(self):
		return self.__money
	def setMoney(self,money):
		if money <= 0:
			print("传入金额非法")
		else:
			self.__money = money

xiaoming = Person()
xiaoming.setMoney(20)
print(xiaoming.getMoney())


	def getMoney(self):
		return self.__money
	def setMoney(self,money):
		if money <= 0:
			print("传入金额非法")
		else:
			self.__money = money
