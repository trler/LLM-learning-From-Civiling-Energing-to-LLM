def function_1():
    pass


class CuteDog:
    """一次模拟小狗"""
    def __init__(self, name, age):  # 初始化方法 不需要显式调用
        """初始化属性 name 和 age"""  # 类里面的函数就是方法
        self.name = name
        self.age = age
    
    def sit(self):
        """模拟小狗收到命令时会坐下"""
        print(f"{self.name}坐下来")

    def roll_over(self):
        print(f"{self.name}在打滚")
        
my_dog = CuteDog("大狗大狗", '叫叫叫')
my_dog.sit()
my_dog.roll_over()
print(my_dog.age)


# 修改实例属性的方式
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"

        return long_name.title()
    
    def read_odometer(self):
        print(f"这辆车已经行驶了{self.odometer_reading}公里")

    def update_odometer(self, kelometer):
        self.odometer_reading = kelometer
    
    def increment_odometer(self, kelometer):
        self.odometer_reading += kelometer

my_new_car = Car("audi", "a4", 2025)
msg = my_new_car.get_descriptive_name()
print(msg)

# 修改属性的值 通过对象修改 通过类方法设置 通过类方法递增 
my_new_car.odometer_reading = 24
my_new_car.read_odometer()

my_new_car.update_odometer(58)
my_new_car.read_odometer()


# 继承 写七八个类,有相同属性,就可以用继承 super()来调用父类的属性 

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

class Battery:
    def __init__(self, size=40):
        self.battery_size =size

    def describe_battery(self):
        print(f"这辆车的电池容量是{self.battery_size} -kwh")



my_leaf = ElectricCar("nissan", "leaf", 2024)
print(my_leaf.make)

# 给子类定义属性和方法

# 重写父类方法 定义一个同名的方法就可以了 优先级为 python先查找子类中的方法 
print(my_leaf.battery.battery_size)
my_leaf.battery.describe_battery()