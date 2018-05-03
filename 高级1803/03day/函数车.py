class Car():
	def __init__(self,color):
		self.color=color
	def __str__(self):
		a = "车的颜色是%s"%self.color
		return a

	def come(self):
		print("车在走")
	def stop(self):
		print("车停啦")
bmw = Car("白色")
print(bmw)
bmw.come()
bmw.stop()

