magics = ['alice', 'david', 'caro']
for magic in magics:
    print(magic)

# 4.1.2 for 循环执行更多操作
    print(f"你好{magic.title()}!")
    print(f"你的表演爱好了，瞎猜还想看{magic.title()}的表演")


print("\n你们可以怕了")

# 避免缩进错误 所有的内容都应该在循环体内，多余的符号也要折叠回去

# 4.3 创建数值列表  rang([start,] end [,step]): 生成可以迭代的数值列表表示 [] 里面是科讯参数，意思是可以不传入
# python 已经可以处理好了默认不传的情况

for num in range(0,6,1):  # 左闭右开的环节
    print(num)
for num in range(5):
    print(num)
for Num in range(0,60,5):
    print(Num)
for num in range(60,0,-5):
    print(num)

# 创建一个空列表，并传值
squares = []
for val in range(1,11):
    squares.append(val ** 2)
print(squares)

# 4.3.1 列表推导式 python 特有语法

# squares = [val ** 2 for val in range(100,2,-5)]
# print(squares)

# 4.3.2 数值列表简单统计计算 sum max min
print(min(squares))
print(max(squares))
print(sum(squares))

# 4.4 使用列表的一部分 slice 处理列表中部分元素 在索引中用冒号：
players = ['张三', 'xiaohong', 'nanyun', 'chuixu1', 'wuzang']

print(f'原版的列表:{players}')
print(f'players[0:3]:{players[0:3]}')
print(f'players[1:3]:{players[1:3]}')
print(f'players[:3]:{players[:3]}')
print(f'players[2:]:{players[2:]}')
print(f'players[-2:]:{players[-2:]}')

# 4.4.1 深拷贝 全新变量指向全新内存区域
players_1 = players[:]

print(id(players))
print(id(players_1))

# 4.5 元祖 tuple 不可变列表（）表示 无法修改
dim = (200, 5)
# 也可以用for循环来遍历

# 4.6 设置代码格式 每行不超过79个字符 代码不同部分隔开， 赋值 打印
prompt = """你好，我是你的大脑你好，我是你的大脑你好，
            我是你的大脑你好，我是你的大脑你好，
            我是你的大脑
            """


print(prompt)

