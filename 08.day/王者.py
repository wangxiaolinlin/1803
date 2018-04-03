zhanghao = '123'
mima = '123'
count = 0
a = True
while a:
	zh = input('请输入账号: ')
	mm = input('请输入密码: ')
	if zh == zhanghao and mm == mima:
		print('登录成功')
		yx = int(input('请选择英雄 0:ADC 1:肉 2:法师'))
		if yx == 0:
			print('鲁班')
		elif yx == 1:
			print('程咬金')
		elif yx == 2:
			print('王昭君')
		a = False
	else:
		print('账号或密码错误')
		count += 1
		if count == 3:
			a = False
			print('输入次数过多，退出')
