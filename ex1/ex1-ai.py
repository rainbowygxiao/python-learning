# 获取用户输入的两个整数列表
a1 = list(map(int, input("请输入第一个整数列表（用空格分隔）：").split()))
a2 = list(map(int, input("请输入第二个整数列表（用空格分隔）：").split()))

# 将列表转换为集合
set1 = set(a1)
set2 = set(a2)

# 向集合中添加重复元素
set1.update(a1)
set2.update(a2)

# 输出集合
print("第一个集合（添加重复元素后）：", set1)
print("第二个集合（添加重复元素后）：", set2)

# 分别输出两个集合
print("第一个集合：", set1)
print("第二个集合：", set2)

# 交换两个集合的赋值
set1, set2 = set2, set1

# 再次输出
print("交换后第一个集合：", set1)
print("交换后第二个集合：", set2)