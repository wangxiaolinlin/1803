def a(x,y):
	return x + y
#相加
def b(x,y):
	return x - y
#相减
def c(x,y):
	return x * y
#相乘
def d(x,y):
	return x / y
#相乘

print('选择运算:')
print('1,相加')
print('2,相减')
print('3,相乘')
print('4,相除')

shu = input('请输入数字(1/2/3/4):')
num1 = int(input('请输入第一个数字:'))
num2 = int(input('请输入第二个数字:'))
if shu == '1':
	print(num1,'+',num2,'=',a(num1,num2))
elif shu == '2':
	print(num1,'-',num2,'=',b(num1,num2))
elif shu == '3':
	print(num1,'*',num2,'=',c(num1,num2))
elif shu == '4':
	print(num1,'/',num2,'=',d(num1,num2))
else:
	print('非法输入')
