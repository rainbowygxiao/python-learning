a1 = input("请输入第1个整数列表（用逗号分隔）：")
a2 = input("请输入第2个整数列表（用逗号分隔）：")
l1 = a1.split(",")
l2 = a2.split(",")

b1=set(l1)
b2=set(l2)
print("第一个集合1:",b1)
print("第二个集合1:",b2)

a11 = input("请输入第1个整数列表（用逗号分隔）：")
a21 = input("请输入第2个整数列表（用逗号分隔）：")
l11 = a11.split(",")
l21 = a21.split(",")

for i in range(len(l11)):
    b1.add(l11[i])
for i in range(len(l21)):
    b2.add(l21[i])

print("第一个集合2:",b1)
print("第二个集合2:",b2)
a = b1
b1=b2
b2=a
print("第一个集合2:",b1)
print("第二个集合2:",b2)