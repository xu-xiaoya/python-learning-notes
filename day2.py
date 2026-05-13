# 输入字符串
name=input('your name:')
print(f"hello! {name}")
# 输入数字
age=input('your age:')
age=int(age)
print(age)

# while循环
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

# 列表遍历+修改 
    
        
