def sushu(a):#定义一个函数里面随便参
	list = []#创建一个空列表
	for i in range(100,a):
		w = True
		for j in range(100,i):
			if i%j == 0:
				w = False
				break
		if w:
			list.append(i)#列表添加
	print(list)#输出列表
sushu(201)#调用 里面参数
