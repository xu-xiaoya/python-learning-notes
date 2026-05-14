from name_function import get_formatted_name

# 单元测试
def test_first_last_name():
    formatted_name = get_formatted_name('janis', 'joplin')
    # assert断言：声称满足特定的条件
    assert formatted_name == 'Janis Joplin'

def test_first_last_middle_name():
    formatted_name = get_formatted_name(
        'wolfgang', 'mozart', 'amadeus')
    assert formatted_name == 'Wolfgang Amadeus Mozart'