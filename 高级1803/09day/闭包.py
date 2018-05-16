
def test(a):
	def test1(c):
		print(a+c)
	return test1
f = test(1)
f(2)

"""
def line_conf(a,b):
	def line(x):
		return a*x+b
	return line
f = line_conf(5,6)
print(f(1))
print(f(2))
"""
