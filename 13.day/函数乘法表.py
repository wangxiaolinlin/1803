def chengfa(b):
	for i in range(1,b):
		for j in range(1,i+1):
			print("%d*%d=%d"%(i,j,i*j),end = " ")
		print("")
chengfa(10)

