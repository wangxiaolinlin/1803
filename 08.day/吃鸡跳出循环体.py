count =int(input('请输入一个数字'))
ouhe = 0
jihe = 0
x = 0
while x < count:
	print('当前数字:%d'%x)
	x += 1
	if x%2 == 0:
		ouhe = ouhe + x
	elif x%2 != 0:
		jihe = jihe + x
print('偶数和为:%d'%ouhe)
print('基数和为:%d'%jihe)
print('总和为:%d'%(ouhe+jihe))
