def sum_day(date):
	year = int(date[0:4])
	month = int(date[4:6])
	day = int(date[6:])
	flag = 0
	if (year%4==0 and year%100!=0 ) or year%400 == 0:
		flag = 1
	big_month = [1,3,5,7,8,10,12]
	small_month = [4,6,9,11]
	for i in range(1,month):
		if i in big_month:
			all_day+=31
		elif i in small_month:
			all_day+=30
		if i == 2 and flag == 1:
			all_day+=29
		elif i==2:
			all_day+=28
	all_day+=day
	print("天数是%d"%all_day)
sum_day()
