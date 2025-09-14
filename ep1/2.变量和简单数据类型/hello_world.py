message = "Hello Python World!!"
print(message)

message = "Hello World!!"
print(message)

Message = " hello world!!"

# 一般不用IO来命名,让人看错为数字

张三 = "helloworld!"

# 中文也不要用

# 方法名

name = "ada lovelace"
print(name.title())
print(name.upper())

# 快速格式化

first_name = "张"
last_name = "三"

total_name = f"{first_name}{last_name}"
print(total_name)


#  特殊字符串 \t 制表符 \n 换行符 

str_1 = " Python \t rust\n" \
        "11 \t ws     "
str_2 = "   Python \n " 

print(str_1)
print(str_2)

# 删除空白 lstrip() rstrip() strip() 分别删除两端的空白

print(str_1.strip())
print(str_2.lstrip())    

# 删除前缀  比如需要删除网站 http的前缀 remove

url = "https://github.com/trler/LLM-learning-From-Civiling-Energing-to-LLM.git"
url = url.removeprefix("https://")
print(url) 

# 2.3.6 字符串语法错误, 单引号双引号错误 交叉使用

# 2.3.7 字符串拼接 *生成重复字符串

message = "hello" +" "+ "Wolrd" + "!!!"*100

print(message)

# 整数浮点数 int float

num_1 = 1.542
num_2 = 1_000_222_1

print(num_1)
print(num_2)

# 2.4.1 数运算 + - * ** / //  >> << 位运算 二进制向右移动或向左移动
# 向右移动 为整除了 2的n次方 向左乘2的n次方

# 2.4.3 python 可以同时给多个变量赋值

x, y, z = 1, 2, 3
print(f"x={x}")
print(f"y={y}")
print(f"z={z}")

# 常量 constant 用全大写表示

MAX_CONNECTIONS = 5000

# 注释 用# 表示
# 写注释 
print("写注释")  # 何意味

# 2.5.1 该编写什么样的注释

# 2.6 Python之禅

import this
 