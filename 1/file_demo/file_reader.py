from pathlib import Path

path = Path('pi_million_digits.txt')
content = path.read_text()
print(content)


# 访问文件的每行,将每一行存入列表
lines = content.splitlines()
pi_string = ''
for line in lines:
    print(line)
    pi_string += line.strip()

print(f"{pi_string[:52]}....")
print(len(pi_string))
# 使用文件中的内容 利用 

# 圆周率中有生日吗 in关键字

birthday = input("输入你的生日,格式如括号中(yymmdd): ")
if birthday in pi_string:
    print("你的生日出现在了圆周率中!")
else:
    print("失败")


# with 语句 with 关键字来打开文件并执行一些读取,写入操作
# with open(文件名,模式) as 文件对象:
#     文件对象.方法
with open('pi_million_digits.txt', 'r' ,encoding='UTF-8') as file:
    print(file.read())

path = Path('ham.txt')
content = '哈哈'
path.write_text(content, "utf-8")

# try-except
try:
    print(5/ 0)
except Exception as e:
    print("e")


