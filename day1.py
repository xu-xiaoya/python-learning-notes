"""Day 1: Python data types and basic operations."""

def print_section(title: str) -> None:
    print(f"\n===== {title} =====")


def demo_strings() -> None:
    print_section("字符串")

    first_word = "hello"
    second_word = "world"
    full_message = f"{first_word} {second_word}"
    print(full_message.upper(), full_message.lower(), full_message.title())

    # 去除空格
    message_with_space = " python "
    print(
        message_with_space.strip(),
        message_with_space.lstrip(),
        message_with_space.rstrip(),
    )

    # 打印数字包裹str
    age = 2
    birthday_message = f"happy {age}nd birthday"
    print(birthday_message)

# 运算符号
def demo_numbers() -> None:
    print_section("数字与运算")

    age = 2
    result = age**3
    print(result)  # 2^3 = 8
    print(3 % 2)   # 1，可以用来判断奇偶
    print(6 % 3)   # 0

# 列表 
def demo_lists() -> None:
    print_section("列表")

    numbers_in_french = ["un", "deux", "trois", "quatre"]
    numbers_in_french[3] = "quatre_"
    ''' 访问元素（-1代表倒数第一个）'''
    print(numbers_in_french[0], numbers_in_french[-1])

    ''' 添加元素 '''
    numbers_in_french.append("six")
    print(numbers_in_french)

    ''' 在索引x的位置添加元素 '''
    numbers_in_french.insert(4, "cinq")
    print(numbers_in_french)

    ''' 删除元素 '''
    # 已知索引
    del numbers_in_french[0] 
    print(numbers_in_french)

    # 删除末尾，并拿到该元素(类比弹出栈顶元素)
    popped_item = numbers_in_french.pop() 
    print(popped_item, numbers_in_french)

    # 删除指定位置元素并拿到该元素
    first_item = numbers_in_french.pop(0)
    print("first number has popped:", first_item)

    # 根据值删除
    numbers_in_french.remove("trois")
    print(numbers_in_french)

# 排序
def demo_sorting() -> None:
    print_section("排序")

    cars = ["bmw", "audi", "toyota", "subaru"]

    # 按字母排序 
    ''' 不改变原数组 '''
    print(sorted(cars), "原数组:", cars)
    print(sorted(cars, reverse=True), "原数组:", cars)
    ''' 改变原数组 '''
    cars.sort()
    print("升序排序后:", cars)

    cars.sort(reverse=True)
    print("降序排序后:", cars)

    # 仅反转列表
    cars.reverse()
    print("反转后:", cars)
    # 长度
    print("长度:", len(cars))

def demo_slices_and_copies() -> None:
    print_section("切片与复制")

    # 切片【指定使用的第一个元素和最后一个元素的index】
    players = ["A", "B", "C", "D", "E"]
    print(players[0:3]) 
    print(players[:4]) #从头开始
    print(players[2:]) #到尾截至
    print(players[-2:]) #输出最后2个元素

    # 复制
    ## 引用地址相同
    shared_players = players
    shared_players.append("F")
    print("直接赋值:", shared_players, players) # 两个都加上了F

    ## 复制副本，引用地址不同
    copied_players = players[:]
    copied_players.append("G")
    print("切片复制:", copied_players, players)

# 元组
# 定义：不能修改的值称为不可变的，不可变的列表就是元组 (xx, xx, xx)
def demo_tuples() -> None:
    print_section("元组")

    dimensions = (200, 50)
    print(dimensions[0])
    # dimensions[0]=10 元素不允许修改

    for dimension in dimensions:
        print(dimension)

    # 可以赋值整个元组
    dimensions = (400, 100)
    for dimension in dimensions:
        print(dimension)

# 字典
# 定义：一系列键值对，值可以是任意python对象 {key: value}
def demo_dictionaries() -> None:
    print_section("字典与集合")

    person = {"color": "yellow", "money": "10000"}
    # 访问key的值
    print(person["money"])
    '''  ✔推荐，若指定key不存在情况可以防止报错 '''
    point_value = person.get("point", "No point value assigned")
    print(point_value)

    # 修改
    person["color"] = "green"
    # 添加键值对
    person["name"] = "yaya"
    person["point"] = "10000"
    print(person)
    # 删除键值对
    del person["color"]
    print(person)

    # 遍历key+value
    for key, value in person.items():
        print(f"key: {key} value: {value}")

    # 遍历keys 默认person=person.keys() keys()可忽略
    for key in sorted(person):
        print(key.title())
    
    # 遍历values
    # 为剔除重复项，可使用集合(set)。
    
    for value in set(person.values()):
        print(value)
    # 集合
    # 定义：集合中的每个元素都必须是独一无二的，只有value， {xx, xx, xx}

    # 字典列表
    alien_0 = {"color": "green", "points": 5}
    alien_1 = {"color": "yellow", "points": 10}
    alien_2 = {"color": "red", "points": 20}
    aliens = [alien_0, alien_1, alien_2]
    print("字典列表:", aliens)

    # 字典字典
    users = {
        "yaya": {"first": "xu", "last": "yaya"},
        "lala": {"first": "wu", "last": "lala"},
    }
    print("字典嵌套字典:", users)


def main() -> None:
    demo_strings()
    demo_numbers()
    demo_lists()
    demo_sorting()
    demo_slices_and_copies()
    demo_tuples()
    demo_dictionaries()


if __name__ == "__main__":
    main()
