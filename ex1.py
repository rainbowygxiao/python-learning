a1 = input("请输入第1个整数列表（用逗号分隔）：")
a2 = input("请输入第2个整数列表（用逗号分隔）：")
l1 = list(map(int,a1.split(",")))
l2 = list(map(int,a2.split(",")))

b1=set(l1)
b2=set(l2)
print("第一个集合1:",b1)
print("第二个集合1:",b2)

b1.update(l1)
b2.update(l2)
print("第一个集合2:",b1)
print("第二个集合2:",b2)
tmp = b1
b1=b2
b2=tmp
print("第一个集合2:",b1)
print("第二个集合2:",b2)