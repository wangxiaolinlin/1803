class digua():
	def __init__(self):
		self.shengshu = 0
		self.cookstr = '生的'
		self.condliments = []
	def cook(self,time):
		self.shengshu+=time
		if self.shengshu > 8:
			self.cookstr = "烤糊了"
		elif self.shengshu > 5:
			self.cookstr = "烤好了"
		elif self.shengshu > 3:
			self.cookstr = "半生不熟"
		else:
			self.cookstr = "生的"



kaodigua = digua()
kaodigua.cook(5)
print(kaodigua.shengshu)
print(kaodigua.cookstr)

