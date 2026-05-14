"""Day 2: Python flow control, input, and loop practice."""

def print_section(title: str) -> None:
    print(f"\n===== {title} =====")

# if/ elif / else
def get_ticket_price(age: int) -> int:
    if age < 4:
        return 0
    if age < 26:
        return 18
    return 40

# 条件判断 = > >= < <= != ==
def demo_conditions() -> None:
    print_section("条件判断")

    car = "bmw"
    print(car.lower() == "bmw") # True
    print(car.lower() != "audi") # True

    # and / or
    age_0 = 25
    age_1 = 10
    print(age_0 >= 21 and age_0 < 50)
    print(age_0 < 50 or age_1 > 30)

    # in / not in
    foods = ["beef", "chicken", "milk"]
    print("milk" in foods)
    if "salade" not in foods:
        print("no!!")

    print(f"cost {get_ticket_price(age_0)}$")

# 循环
def demo_for_loops_and_ranges() -> None:
    print_section("for in 循环与 range")

    fruits = ["pommes", "bananes", "ananas"]
    for fruit in fruits:
        print(f"{fruit} c'est delicieuse!")
    print("j'aimerais les acheter!")

    for value in range(1, 5):
        print(value) # 不包含5

    # 创建数字列表
    numbers = list(range(1, 6))
    print(numbers) # [1,2,3,4,5]

    even_numbers = list(range(2, 11, 2)) # 从2开始，指定步长2
    print(even_numbers) # [2,4,6,8,10]

    # 数字列表简单计算
    print("最小值:", min(even_numbers))
    print("最大值:", max(even_numbers))
    print("总和:", sum(even_numbers))

    # 【写法】列表解析
    squares = [value**2 for value in range(1, 11)]
    print("平方列表:", squares)

# 多个列表判断
def demo_loop_with_conditions() -> None:
    print_section("循环中的条件判断")

    available = [
        "mushrooms",
        "olives",
        "green peppers",
        "pepperoni",
        "pineapple",
        "extra cheese",
    ]
    requested = ["mushrooms", "french fries", "extra cheese"]

    for requested_item in requested:
        if requested_item in available:
            print(f"adding {requested_item}")
        else:
            print(f"sorry, don't have {requested_item}")
    print("finish!")

# 输入
def greet_user() -> None:
    print_section("输入 input()")

    # 输入字符串
    name = input("your name: ").strip()
    print(f"hello! {name}")

    # 输入数字
    age = input('your age:').strip()
    age = int(age)
    print(age)


# while循环
def number_game(target: int = 10) -> None:
    print_section("while 循环")

    while True:
        message=input('enter:')
    
        if message=='quit':
            break
        else:
            number=int(message)
            print(message)
            if number != 10:
                continue
            else:
                print('you got it!') 
                break


def confirm_users(unconfirmed_users: list[str]) -> list[str]:
    waiting_users = unconfirmed_users[:]
    confirmed_users: list[str] = []

    while waiting_users:
        current_user = waiting_users.pop()
        confirmed_users.append(current_user)

    return confirmed_users


def remove_all_occurrences(items: list[str], value: str) -> list[str]:
    return [item for item in items if item != value]

# 列表遍历+修改 
def demo_list_processing() -> None:
    print_section("列表处理练习")

    unconfirmed_users = ["alice", "bob", "charles"]
    confirmed_users = confirm_users(unconfirmed_users)
    print("confirmed users:", confirmed_users)

    pets = ["dog", "cat", "dog", "fish", "cat"]
    pets_without_cats = remove_all_occurrences(pets, "cat")
    print("pets after removal:", pets_without_cats)


def main() -> None:
    demo_conditions()
    demo_for_loops_and_ranges()
    demo_loop_with_conditions()
    greet_user()
    number_game()
    demo_list_processing()


if __name__ == "__main__":
    main()
