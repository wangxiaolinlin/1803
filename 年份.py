year = int(input('请输入一个年份'))
if year > 0:
	if year%4 == 0 and year%100 != 0:
		print('这是闰年')
	elif year %400 == 0:
		print('这是闰年')
	else:
		print('平年')
else:
	print('输入有误')
