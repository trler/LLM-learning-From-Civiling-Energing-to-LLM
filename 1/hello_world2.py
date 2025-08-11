msg = ''
if msg:
    alien_0 = {
        'color': 'green',
        'points': 5
    }
    print(alien_0['color'])

    alien_0['color'] = 'yellow'

    print(alien_0['color'])
alien_0 = {
    'color': 'green',
    'points': 5
}
print(alien_0['color'])

alien_0['color'] = 'yellow'

print(alien_0['color'])    

del alien_0['points']
print(alien_0)

# 由类似对象组成的字典 一个对象的多种信息，颜色，击杀分数，xy坐标 \\ 多个对象的同一种信息 谁使用了什么编程语言

# 使用get 方法来访问值 如果指定的键不存在，那么之前的访问方式就会出现keyerror错误 
# get方法可以使用 dict.get("speed") 返回一个None

print(alien_0.get("speed",'键不存在'))

# 遍历所有键值对 d.items() 返回键值对的元祖视图 返回的是一个元祖
for key, value in alien_0.items():
    print(f"{key}对应的值是{value}")
# key, value = ("color", "green")

# 遍历字典中所有键 kes方法
alien_0 = {
    'color': 'green',
    'points': 5
}
for key in alien_0.keys():
    print(f"{key}")

for value in alien_0.values():
    print(f"{value}")

# 列表中中存储字典
alien_0 = {
    'color': 'green',
    'points': 5
}
alien_1 = {
    'color': 'yellow',
    'points': 7
}
alien_2 = {
    'color': 'red',
    'points': 10
}
aliens = [alien_0, alien_1, alien_2]
print(aliens)

# 字典中嵌套列表
steak = {
    '做法': '五分熟',
    '配菜': ['菠菜', '西兰花']
}
for vagetable in steak['配菜']:
    print(vagetable)

# 字典中嵌套字典
users = {
    '峰哥亡命天涯':{
        '姓': '周',
        "名": '丽峰',
        '居住地': '深证'
    },
    '大猛子':{
        '姓': '印',
        '名': '猛',
        '居住地': '东北'
    }
}