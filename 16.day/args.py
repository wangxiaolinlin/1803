"""
def sum(a,b,*args,**kwargs):
	all_sum+=a
	all_sum = all_sum+a
	print(all_sum)

t = (3,4,5)
d = {"date":6}
"""


num = 10
def test(num):
	num+=num
	print(num)
a = [100]
def test1(a):
	a+=a
	a=a+a
	print(a)
test(num)
print(num)
test1(a)
