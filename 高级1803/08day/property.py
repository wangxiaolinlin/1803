class Laowang(object):
	def __init__(self):
		self.__money = 1000
	@property
	def money(self):
		return self.__money
	@money.setter
	def money(self,money):
		self.__money = money
laowang = Laowang()
laowang.money = 497
print(laowang.money)



class Laowang(object):
	def __init__(self):
		self.__money = 1000
	@property
	def money(self):
		return self.__money
	@money.setter
	def money(self,money):
		self.__money = money

laowang = Laowang()
laowang.money = 1000
print(laowang.money)
