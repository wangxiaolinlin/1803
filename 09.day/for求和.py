"""
i = 0
for a in range(1,101):
	i =i+a
print("0到100总和是%d"%i)
"""

for i in range(1,5001):#同时能被5和7整除的数字
	if i%5 == 0 and i%7 == 0:
		print(i,end=" ")
