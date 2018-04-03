import random
s = random.randint(1,100)
a = 1
while a<11:
	c = int(input('请输入数字:'))
	if c > s:
		print('比%d小'%c)
	elif c < s:
		print('比%d大'%c)
	elif c == s:
		print('猜中了')
		break
	a += 1
