class Dog():
	def __init__(self,name):
		print("init方法在这")
		self.name = name
	def jiao(self):
		print("狗在叫")
	def run(self):
		print("狗在跑")
	def __del__(self):
		print("del方法被调用")
		print("对象%s马上被删掉了"%self.name)
taidi = Dog("王润泽")
hashiqi = taidi
del(taidi)
del(hashiqi)
print("看见看见啥地方快捷方式看见看见")
