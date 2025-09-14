def print_number():
    ''' 
    呵呵,您已经死了
    '''
    for i in range(5):
        print(i)
    
print_number()
print(print_number)

def function_1():
    # TODO 实现图像人脸检测 + 剪裁功能
    pass

def function_2():
    # TODO 实现图像人脸检测 + 剪裁功能
    pass

def function_3():
    # TODO 实现图像人脸检测 + 剪裁功能
    pass

def function_4(name, age=18):
    print(f"{name}的年龄是{age}")

function_4('张三')


def function_5(names, age=18):  # 默认值
    
    for name in names:
        print(f"{name}的年龄是{age}")

function_5(["张三", "嘻嘻"], 25)
function_5(age=52,names=["张三", "嘻嘻"])  # 传关键字实参

# 要避免实参错误 提供的实参多余活少于需要的参数时候  关键字实参必须在位置实参后面

# 作用域 全局作用域和局部作用域 变量的

# 返回值

# 结合函数 和while 循环

def comput_circle_area(radius):
    area = 3.14 * radius ** 2

    return area

while True:
    radius = input("请输入圆的面积(输入'q'退出): ")

    if radius == 'q':
        break
    else:
        radius = int(radius)
        print(f"圆的面积为{comput_circle_area(radius=radius)}")

# 向函数传递列表

# 传递任意数量的形参 不知道要有多少参数参入 
def order_dishes(name, *dishes): # 打包为一个元组
    print(f"你好,{name},您点了: ")  
    for dish in dishes:  # for循环遍历元组
        print(f" - {dish}")
    
order_dishes("张三", "牛乳", "呵呵", "搜索")

# 使用任意数量的关键字实参  不知道信息是什么样子的 刚刚那个不需要形参名字, 这个不但不知道实参的数量

def build_profile(first_name, last_name, **user_info):
    user_info["first_name"] = first_name
    user_info["last_name"] = last_name

    return user_info


print(build_profile("阿尔布特", "爱因斯坦", location = '普林西普' , field = "物理" ))









