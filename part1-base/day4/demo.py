"""Day 4 demo runner."""

from .car import Car
from .dog import Dog
from .electric_car import ElectricCar


# 类: 一个模板，用来描述一类事物
##   对象: 根据类创建出来的具体实例
##   属性: 对象身上的数据，比如 name、age
##   方法: 对象可以执行的动作，比如 sit()、roll_over()


def print_section(title: str) -> None:
    print(f"\n===== {title} =====")


# 创建对象
def demo_dog_class() -> None:
    print_section("创建对象")

    my_dog = Dog("doudou", 3)
    your_dog = Dog("nini", 5)

    print(f"My dog's name is {my_dog.name}.")
    print(f"My dog is {my_dog.age} years old.")
    my_dog.sit()
    my_dog.roll_over()

    print(f"Your dog's name is {your_dog.name}.")
    print(f"Your dog is {your_dog.age} years old.")


# 属性修改
def demo_change_attribute() -> None:
    print_section("属性修改")

    my_car = Car("tesla", "model 3", 2024)
    my_car.describe_car()
    my_car.read_mileage()

    my_car.update_mileage(120)
    my_car.read_mileage()


# 组合: 一个类里面“组合”另一个类的对象
def demo_inheritance_and_composition() -> None:
    print_section("继承、重写与组合")

    my_electric_car = ElectricCar("tesla", "model y", 2025)
    my_electric_car.describe_car()
    my_electric_car.read_mileage()
    my_electric_car.battery.describe_battery()


def main() -> None:
    demo_dog_class()
    demo_change_attribute()
    demo_inheritance_and_composition()
