#coding = utf-8
zhanghao = '123'
mima = '123'
count = 0
a = True
while a:
	zh = input('q 王')
	mm = input('a: ')
	if zh == zhanghao and mm == mima:
		print('yes')
		yx = int(input(' 0:ADC 1: 2:'))
		if yx == 0:
			print('b')
		elif yx == 1:
			print('cyj')
		elif yx == 2:
			print('wzj')
		a = False
	else:
		print('no')
		count += 1
		if count == 3:
			a = False
			print('gun')
