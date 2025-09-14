# 5.1 
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.title())
    else:
        print(car.upper())

# 5.2.1 条件测试 相等 == != > >- < <=
car = 'Audi'
print(car == 'audi')
print(car.upper() == car)

# 布尔运算 and or
age_0 = 22
age_1 = 18

print(f"age_0 >= 21 and age_1 >= 21的结果是: {age_0 >= 21 and age_1 >= 21}" )
print(f"age_0 >= 21 or age_1 >= 21的结果是: {age_0 >= 21 or age_1 >= 21}" ) 

# 布尔运算 not in\\ not true == false \\in 用来检查特定值是否在集合
request_toppings = ['蘑菇','泽村']

print('蘑菇' in request_toppings)
print('bocai' in request_toppings)

print("蘑菇" not in request_toppings)
print('菠菜' not in request_toppings)

# 5.3 if 语句 if-else  if-elif-else
score = 75

if score < 60:
    print("对不起，下次再见")
elif score == 60:
    print("这次放过你")
elif 60 < score < 70:
    print("您获得D")
    print("恭喜你通过考试")
elif 70 <= score < 80:
    print("您获得C")
    print("恭喜你通过考试")
elif 80 <= score < 90:
    print("您获得B")
    print("恭喜你通过考试")
else:
    print("您获得A")
    print("恭喜你通过考试")

# 也可以创建多个if块，来检查想要的所有条件
 
# 确定非空列表 列表名也能当做条件表达式 只有当列表至少包含一个元素才ture

request_addings = []
msg = ""

if msg:
    for request_topping in request_addings:
        print(f"已加入{request_topping}")
else:
    print("你确定什么都不要吗")



lst.sort()