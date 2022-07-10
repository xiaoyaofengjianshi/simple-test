a = int(input("请输入乘法表首位："))
b = int(input("请输入乘法表末位："))
pass
for i in range(a,b+1):
	for x in range(1,i+1):
		print(i,"*",x,"=",i*x,end="\t")
	print("\n")
input("按任意键退出程序。")