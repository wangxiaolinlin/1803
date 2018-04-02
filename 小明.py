shengao = int(input('请输入你的身高: '))
heigt = int(input('请输入你的体重: '))
a = (heigt/(shengao*shengao))
if a < 18.5:
	print('低于18.5,过轻')
elif a > 18.5 and a < 25:
	print('正常')
elif a < 32:
	print('严重肥胖')
