zhanghao = '969423814'
mima = '123'
zh = input('请输入您的银行卡账号: ')
mm = input('请输入您的银行卡密码: ')
if zh == zhanghao and mm == mima:
	qu = int(input('登陆成功,请输入取款金额: '))
	if qu > 100:

		qian = 100
		print('没钱取毛线')
	elif qu < 100:
		qian = 100
		print('取钱成功剩余%d元'%(qian-qu))
else:
	print('账号或密码不正确')

