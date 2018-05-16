class Ba():
	def momey(self):
		print("双手赚钱")
class Son(Ba):
	def money(self):
		print("脑子赚钱")
		super().momey()
a = Son()
a.money()
