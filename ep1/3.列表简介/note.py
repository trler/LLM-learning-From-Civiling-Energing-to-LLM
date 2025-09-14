# 建议给列表指定一个表示复数的名称 比如letters, digits.

# 3.1.1 访问列表元素 通过下表索引[0] 
# 负数索引是指几个元素 -1 表示倒数第1个
bike = ['bike_1', "bike_2", "bike_3"]

print(bike[0])
print(bike[-1])

# 3.1.2 列表的值可以使用的,f-字符串中,可以用列表中的值来打印消息

bikes = ['aA', 'B', 'C']
msg = f"The bike brand is {bikes[0].title()}"

print(msg)

# 3.2.1 修改列表元素 首先要指定 列表名, 要修改的元素索引 新的值

motocycles = ['honda', 'yamaha', 'suzuki']

motocycles[0] = 'yadi'

print(motocycles)
print(motocycles[0])

# 3.2.2 列表中添加元素 list.append 末尾添加 lst.insert 在索引处添加
motocycles.append('dult')
print(motocycles)

motocycles.insert(0,'heyiwei')
motocycles.insert(0,'heyiwei')
print(motocycles)

# 3.2.3 从列表删除元素 del list[]删除指定索引处元素 lst.pop 删除并返回列表中指定索引 默认为尾部
del motocycles[0]
print(motocycles)

poped_biked = motocycles.pop()
print(motocycles)
print(poped_biked)

# 3.3 列表排序 lst.sort() 永久修改原列表 对其中元素进行排序 sorted(lst_1) ->lst_2 返回排序后的列表副本
nums = [9, 5, 6, 55, 2]
nums_1 = sorted(nums)  # 这里会默认正向排序
nums_2 = sorted(nums, reverse=True)
print(nums_1)
print(nums_2)

# 3.3 列表反转 lst.reverse() 修改原列表
print(nums)
nums.reverse()
print(nums)

# 3.4 列表长度 len(lst) -> num 获取列表的元素个数

length = len(nums)

print(length)

# 3.5 避免索引错误 列表索引从0 开始

