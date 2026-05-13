"""Day 4: function """

# def定义函数
''' username是形参, 可设默认值 '''
def greet_user(username='ada'): 
    print(username)
    return username+' hi!'

# 传递列表副本而不是原始列表可以使用[:]

# 不确定参数个数
# 形参名*toppings中的星号让Python创建一个名为toppings的元组，该元组包含函数收到的所有值。
def make_pizza(*toppings):
    print(toppings)
    for topping in toppings:
        print(topping)

# 位置实参+任意实参
def make_pizza_import(size, *args):
    print(f'size:{size}')
    for arg in args:
        print(arg)


def main():
    ''' yaya实参 '''
    greet_user('yaya') 
    
    '''关键字传参，不依赖参数顺序 '''
    greet_user(username='yaya')

    message = greet_user()
    print(message)

    make_pizza('pepper')
    make_pizza('pepper', 'extra cheese', 'mushrooms')


if __name__ == '__main__':
    main()
