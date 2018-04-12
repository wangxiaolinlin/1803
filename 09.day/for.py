start = int(input('请输入一个数字:'))
end = int(input('请输入一个数字:'))
sum = 0
if start < end:
	for i in range(start,end+1):
		print(i)
		sum = sum + i
	print(sum)
else:
	print('输入有误')
