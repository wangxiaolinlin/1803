#创建人类
class Person():
	def __init__(self,name):
		self.name = name
		self.gun = None
		self.hp = 100
	def zhuangzidan(self,danjia,bullet):
		danjia.addBullet(bullet)
	def zhuangdanjia(self,gun,danjia):
		gun.addDanJia(danjia)
	def takeGun(self,gun):#老王拿枪
		self.gun = gun
	def openGun(self,diren):#老王开枪
		#拿到一发子弹
		if diren.hp > 0:#先判断敌人有血还是没血
			zidan = self.gun.popGunBullet()#告诉枪给我一发子弹
			if zidan:
				zidan.kill(diren)#子弹杀人
			else:
				print("没子弹了")
		zidan.kill(diren)#子弹杀人

#创建枪类
class Gun():
	def __init__(self,name):
		self.name = name
		self.danjia = None
	#装弹夹
	def addDanJia(self,danjia):
		self.danjia = danjia
		#print(id(self.danjia))
	def popGunBullet(self):
		return self.danjia.popBullet()
#创建弹夹类
class DanJia():
	def __init__(self,size):
		self.size = size
		self.bullet_list = []
	def addBullet(self,bullet):
		self.bullet_list.append(bullet)#加子弹
		#print(len(self.bullet_list))
	def popBullet(self):
		if self.bullet_list:
			return self.bullet_list.pop()#弹出子弹
		else:
			return None

#创建子弹类
class Bullet():
	def __init__(self):
		self.weili = 5
	#子弹杀人
	def kill(self,diren):
		diren.hp -= self.weili#减去子弹的威力
		if diren.hp <=0:
			diren.hp = 0
			print("%s死了,剩余血量%d"%(diren.name,diren.hp))
		else:
			print("剩余血量为%d"%(diren.name,diren.hp))


laowang = Person("老王")#创建老王对象
ak47 = Gun("ak47")#创建一把枪
danjia = DanJia(20)#放20颗子弹
for i in range(20):#创建20发子弹
	bullet = Bullet()
	laowang.zhuangzidan(danjia,bullet)#装子弹
laowang.zhuangdanjia(ak47,danjia)#装弹夹

laosong = Person("宋祖儿")#创建一个人
laowang.takeGun(ak47)#老王拿枪
laowang.openGun(laosong)
laowang.openGun(laosong)
laowang.openGun(laosong)
laowang.openGun(laosong)
laowang.openGun(laosong)
laowang.openGun(laosong)
laowang.openGun(laosong)
laowang.openGun(laosong)
laowang.openGun(laosong)
laowang.openGun(laosong)
laowang.openGun(laosong)


