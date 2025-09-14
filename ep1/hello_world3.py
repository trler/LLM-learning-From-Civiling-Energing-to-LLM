# #　input() 函数的工作原理
# import math
# name = input("请输入你的名字: ")
# hobby = input('你的爱好是: ')
# year = input('输入你的年龄: ')

# print(f"\n你好, {name},你{year}岁了, 爱好是:{hobby}")

# Warning = "请输入整数"

# r = input("输入圆的半径(int): ")

# r = int(r)
# print(f"圆的面积是: {3.14 *(r ** 2)}")


# # 自赋值运算符
# number = 0
# number = number + 1

# number += 1
# number *= 2
# print(number)


# # 7.1.3 获取值输入
# age = input("请输入年龄: ")
# age = int(age)
# print(age >= 18)

# age = int(age)

# print(age >= 21)

# # 取模

# print(11 % 2)

# # while 循环
# cur_num = 1

# while cur_num < 10:
#     print(cur_num)
#     cur_num += 1

# print("请输入你的名字")
# print("输入'q'退出程序")
# msg = ''
# flag = True  # flag 用flag变量来控制程序循环逻辑 这样能使程序更易于处理多种不同时间导致的停止

# while flag :
#     msg = input()
#     if msg == 'q':
#         flag = False
#     else:
#         print(f"你好,{msg}")

# break 立刻退出循环
cur_num = 1

# while 处理字典列表
uncomfirmed_users = ['张三', '李四', '王五']
confiremed_users = []

while uncomfirmed_users:
    cur_user = uncomfirmed_users.pop()
    print(f"确认用户: {cur_user}")
    confiremed_users.append(cur_user)
print("以下用户都已确认: ")
for comfirmed_user in confiremed_users:
    print(comfirmed_user)

# 循环删除 remove()只能删除首位,然后利用while可以循环删除
pets = ['dog', 'cat', 'dog', 'cat', 'rabbit']

while "cat" in pets:
    pets.remove('cat')

print(pets)