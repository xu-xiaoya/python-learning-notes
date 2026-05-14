"""Dog class examples."""


class Dog:
    # 在__init__方法设定默认值
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def sit(self) -> None:
        print(f"{self.name} is now sitting.")

    def roll_over(self) -> None:
        print(f"{self.name} rolled over!")
