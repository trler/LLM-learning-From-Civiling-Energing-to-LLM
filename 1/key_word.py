# assert finall is lambda rasie yield 
def divide (a, b):
    assert b != 0, "除数不能为0"
    return a / b

result = divide(10, 2)
print(result)

result = divide(10, 8)

# finally raise 关键字
# finally 用来和try except 一起使用 用于定义一个代码块 无论是否发生异常,都会运行,通常用于清理资源
# raise 手动抛出异常, 在接受到并非期望文件格式后提出一个异常,中断程序的正常流程
status = "今天状态不错"
try:
    print("打开 <<Python入门课程, 准备学习\n>>")
    if status != "今天状态不错":
        raise ValueError("看的很慢")

    print("今天又是收货满满的一天")
except Exception as err:
    print(f"根本看不下去,原因{err}, 先吃发吧")

finally:
    print("该吃饭了")


# is关键字 用来比较两个对象身份是否相同 比较内存地址
a = [1, 2, 3]
b = a

print(a == b)  # 他俩的数值相等
print(a is b)  # 他俩是同一个对象
print(id(a))
print(id(b))

b = [1, 2, 3]
print(a == b)  # 他俩的数值相等
print(a is b)  # 他俩是同一个对象
print(id(a))
print(id(b))

# 判断某个对象是否为None
# lambda 关键字 创建匿名函数 lambda: 形参: 表达式

add = lambda x,y : x+y

print(add(3,5))

# 非常pythonid 
# 按照年龄排序
people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]

sorted_perple = sorted(people, key=lambda person: person["age"])
# yield 关键字 定义生成器:
def generate_numbers(n):
    print("函数被执行力")
    for i in range(n):
        yield i, f"这是第{i}次"  # 防止一下吧数据全塞到内存

gen = generate_numbers(5)
# breakpoint()  # 说明并没有实行这个函数调用  # 换成return 就会被执行了

# for num in gen:
#     print(num)

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

# 递归函数 自己调用自己 递归步骤, 将问题分解为更小的子问题,用调用自身来结局这个问题
# 计算阶乘
# def factorial(n):
#     product = 1
#     for i in range(1, n+1):
#         product *= i
    
#     return product


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1) 

print(f"15的阶乘是: {factorial(5)}")

# 递归问题会效率低下
# fib数列
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else: 
        return fibonacci(n-1) + fibonacci(n-2)
    
def func(x: float, y: float) -> int:
    return int(x+y)


print(func(1.3 ,201.1))

num_1 = 5
num_2 = 6
print(num_1.__add__(num_2))
print(num_2 + num_1 )

class person1:
    def __init__(self, salary):
        pass

class DynamicList:
    def __init__(self, elements):
        self.elements = elements
    
    def __len__(self):

        return sum(1 for element in self.elements if element > 0)  # 生成器
    
dynamic_list = DynamicList([10, 2, 23, -3, 1])
print(len(dynamic_list))