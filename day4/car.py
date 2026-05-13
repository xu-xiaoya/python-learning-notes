"""Car class examples."""


class Car:
    def __init__(self, brand: str, model: str, year: int) -> None:
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = 0

    def describe_car(self) -> None:
        print(f"{self.year} {self.brand} {self.model}")

    def read_mileage(self) -> None:
        print(f"This car has {self.mileage} miles on it.")

    def update_mileage(self, mileage: int) -> None:
        if mileage >= self.mileage:
            self.mileage = mileage
        else:
            print("You can't roll back an odometer!")
