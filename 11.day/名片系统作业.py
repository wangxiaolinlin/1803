
list = []
dic = {}
i = 0
while i < 3:
	name = input("请输入姓名")
	age = int(input("请输入年龄"))
	six = input("请输入性别")
	heigt = int(input("请输入体重"))
	i+=1
	dic["name"]=name
	dic["age"]=age
	dic["six"]=six
	dic["heigt"]=heigt
	list.append(dic)
	print(list)
	for o in list:
		for k,v in i.items():
			print("%d:%d"%(k,v))
