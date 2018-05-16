class CarStore(object):
	def createCar(self,typeName):
		pass
	def order(self,type):
		#让工厂根据类型，生产一辆汽车
		self.car = self.createCar(typeName)
		self.car.move()
		self.car.stop()
#定义一个北京现代4s店类
class XiandaiCarStore(CarStore):
	def createCar(self,typeName):
		self.carFactory = CarFactory()
		return self.carFactory.createCar(typeName)
#定义伊兰特车类
class YilanteCar(object):
	#定义车的方法
	def move(self):
		print("车在移动")
	def stop(self):
		print("停车")
#定义索纳塔车类
class SuonataCar(object):
	#定义车的方法
	def move(self):
		print("车在移动")
	def stop(self):
		print("停车")
#定义一个生产汽车的工厂，让其根据具体得订单生产车
class CarFactory(object):
	def createCar(self,typeName):
		self.typeName = typeName
		if self.typeName = "伊兰特"
