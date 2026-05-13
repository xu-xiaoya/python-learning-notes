"""Inheritance and composition examples."""

from .car import Car


class Battery:
    def __init__(self, battery_size: int = 75) -> None:
        self.battery_size = battery_size

    def describe_battery(self) -> None:
        print(f"This car has a {self.battery_size}-kWh battery.")


# 继承: 子类可以直接使用父类的属性和方法
class ElectricCar(Car):
    def __init__(self, brand: str, model: str, year: int) -> None:
        # super可以调用父类的方法
        super().__init__(brand, model, year)
        self.battery = Battery()

    # 重写父类方法: 子类里定义同名方法，会覆盖父类方法
    def describe_car(self) -> None:
        print(f"{self.year} {self.brand} {self.model} (electric car)")
