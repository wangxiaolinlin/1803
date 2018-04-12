list = []
dic = {}
def aa():
	id = input("请输入学生学号::")
	name = input("请输入学生姓名:")
	subjects = input("请输入学科:")
	grade = int(input("请输入分数"))
	dic['id']=id
	dic['name']=name
	dic['subjects']=subjects
	dic['grade']=grade
	list.append(dic)
	print(list)
	for i in list:
		for k,v in i.items():
			print("%s:%s"%(k,v))
def bb():
	find = input("请输入您要查询的学号:")
	for dic in list:
		if find == dic["id"]:
			print("学号:%s 姓名:%s 学科:%s 分数:%s"%(dic['id'],dic['name'],dic['subjects'],dic['grade']))

def cc():
	id = input("请输入您要修改的学生学号:")
	for dic in list:
		if dic["id"] == id:
			kemu = input("请输入您要修改的新科目:")
			dic["subjects"] = kemu
			fen = input("请输入新分数:")
			dic["grade"] = fen
		
			
			guanli = int(input("修改成功，请按2号键查询修改成功""\n欢迎来到学生成绩管理系统，请选择功能1:录入成绩2:查询成绩3:修改成绩4:删除成绩5:退出系统"))
			find = input("请输入您要查询的学号:")
			for dic in list:
				if find == dic['id']:
					print("学号:%s 姓名:%s 学科:%s 分数:%s"%(dic['id'],dic['name'],dic['subjects'],dic['grade']))



def dd():
	id = int(input("请输入您要删除的学号:"))
	a = 0
	for dic in list:
		if dic['id'] == id:
			del list[a]
		else:
			a+=1
		guanli = int(input("删除成功 请按2号键 确认成功\n欢迎来到学生成绩管理系统，请选择功能1:录入成绩2:查询成绩3:修改成绩4:删除成绩5:退出系统 "))
		find = int(input("请输入要查询的学号:"))
		for dic in list:
			if find == dic['id']:
				print("学号:%s 姓名:%s 学科:%s 分数:%s"%(dic['id'],dic['name'],dic['subjects'],dic['grade']))
				print("删除成功")
def ee():
	print("退出")


title = "欢迎进入学生成绩管理系统"
print(title.center(50,"*"))
zhanghao = 969423814
mima = 123
zh = int(input("请输入账号:"))
mm = int(input("请输入密码:"))
if zh == zhanghao and mm == mima:
	print("登录成功，欢迎进入系统")
	print("--------------------------------------------")
	while True:
		guanli = int(input("欢迎来到学生成绩管理系统，\n请选择功能1:录入成绩2:查询成绩3:修改成绩4:删除成绩5:退出系统"))
		if guanli == 1:
			aa()
			t = "-------------------------"
			print(t.center(70,"-"))
		if guanli == 2:
			bb()
			t = "-------------------------"
			print(t.center(70,"-"))
		if guanli == 3:
			cc()
			t = "-------------------------"
			print(t.center(70,"-"))
		if guanli == 4:
			dd()
			t = "-------------------------"
			print(t.center(70,"-"))
		if guanli == 5:
			ee()
			t = "-------------------------"
			print(t.center(70,"-"))
			break
else:
	print("账号或密码错误")
