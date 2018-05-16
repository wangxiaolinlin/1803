石头 = 1
剪刀 = 2
布 = 3
import random
while True:
	diannao = random.randint(1,3)
	me = int(input('请输入 1:石头 2:剪刀 3:布'))
	if me <= 3 and me > 0:
		if (me == 1 and diannao == 2) or (me == 2 and diannao == 3) or (me == 3 and diannao == 1):
			print('你赢啦')
		else:
			print('你输啦')
