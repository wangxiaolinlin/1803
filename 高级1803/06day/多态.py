class Dog(object):
	def __init__(self,name):
		self.name = name
	def game(self):
		print(self.name+"蹦蹦跳跳的玩耍...")
class XiaoTianDog(Dog):
	def game(self):
		print(self.name+"飞到天上去玩耍")
class Person(object):
	def __init__(self,name):
		self.name = name
	def game_with_dog(self,dog):
		print("%s和%s快乐的玩耍..."%(self.name,dog.name))
		dog.game()
feitianwancai = XiaoTianDog("飞天旺财")
xiaoming = Person("小明")
xiaoming.game_with_dog(feitianwancai)
