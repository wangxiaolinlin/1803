class Plane:
	def fei(self):
		print("飞机在天上飞")
	def she(self):
		print("飞机在天上发射子弹")
	def kill(self):
		print("飞机被击落")
feiji = Plane()
feiji.cloer = "白色"
feiji.xinghao = "b1"
feiji.fei()
feiji.she()
feiji.kill()
print(feiji.cloer)
print(feiji.xinghao)
