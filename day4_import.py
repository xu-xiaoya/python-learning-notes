"""Day 4: class import example."""

# 从 day4 文件夹导入类
from day4 import Car, Dog, ElectricCar


def print_section(title: str) -> None:
    print(f"\n===== {title} =====")


def demo_import_dog() -> None:
    print_section("导入 Dog 类")

    my_dog = Dog("cookie", 2)
    print(my_dog.name)
    print(my_dog.age)
    my_dog.sit()


def demo_import_car() -> None:
    print_section("导入 Car 类")

    my_car = Car("byd", "seal", 2024)
    my_car.describe_car()
    my_car.update_mileage(80)
    my_car.read_mileage()


def demo_import_electric_car() -> None:
    print_section("导入 ElectricCar 类")

    my_electric_car = ElectricCar("xiaomi", "su7", 2025)
    my_electric_car.describe_car()
    my_electric_car.battery.describe_battery()


def main() -> None:
    demo_import_dog()
    demo_import_car()
    demo_import_electric_car()


if __name__ == "__main__":
    main()
