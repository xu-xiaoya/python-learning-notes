message="hello"
message1="world"
full_message=message+" "+message1
print(full_message.upper(), full_message.lower(), full_message.title())

# 去除空格
message=" python "
print(message.strip(), message.lstrip(), message.rstrip())

# 打印数字包裹str
age=2
message="happy "+str(age)+"rd birthday"
print(message)
# 运算符号
res=age**3  
print(res) # 2^3=8
## 求模运算符%
3 % 2 # 1 (%2可以用来判断偶/奇数)
6 % 3 # 0

# 列表 
print('===== 列表 ===== ')
arr=['un', 'deux', 'trois', 'quatre']
arr[3]="quatre_"
print(arr[0], arr[-1]) # 访问元素（-1代表倒数第一个）
# ===== 添加 =====
arr.append('six') 
print(arr)
# 在索引x的位置添加元素
arr.insert(4,'cinq') 
print(arr)
# ===== 删除 ===== 
# 已知索引
del arr[0]
print(arr)
# 删除末尾，并拿到该元素(类比弹出栈顶元素)
popped_number = arr.pop()
print(popped_number, arr)
# 删除指定位置元素并拿到该元素
popped_number = arr.pop(0)
print('first number has popped: ', popped_number)
# 根据值删除
arr.remove('trois')
print(arr)

# 排序
print('===== 排序 ===== ')
cars=['bmw','audi','toyota','subaru']
# ====== 按字母排序
# 不改变原数组
print(sorted(cars), "原数组:", cars)
print(sorted(cars, reverse=True), "原数组:", cars)
# 改变原数组
cars.sort()
cars.sort(reverse=True)  # 字母顺序相反排序
print(cars)
# ====== 仅反转列表
cars.reverse()
print(cars)
# ===== 长度
print("长度", len(cars))

# 循环
print('===== 循环 ===== ')
fruits=['pommes', 'bananes', 'ananas']
for fruit in fruits:
    print(fruit+"c'est delicieuse!")
print("j'aimerais les acheter! ")

for value in range(1,5):
    print(value) # 不包含5

# 创建数字列表
numbers=list(range(1,6))
print(numbers) # [1,2,3,4,5]
numbers=list(range(2,11,2)) # 从2开始，指定步长2
print(numbers) # [2,4,6,8,10]

# 数字列表简单计算
min(numbers) #2
max(numbers) #10
sum(numbers) #30

# 【写法】列表解析
squares=[value**2 for value in range(1,11)] # 将1~10提供给表达式value**2

# 切片【指定使用的第一个元素和最后一个元素的index】
players=["A","B","C","D",'E']
print(players[0:3])
print(players[:4]) #从头开始
print(players[2:]) #到尾截至
print(players[-2:]) #输出最后2个元素
# 可以用在循环里
for value in players[:3]:
    print(value) 
## 复制列表
### 引用地址相同
your_players=players
your_players.append('F')
print(your_players, players) # 两个都加上了F
### 复制副本，引用地址不同
my_players = players[:]
my_players.append('G')
print(my_players, players)


# 元组
# 定义：不能修改的值称为不可变的，不可变的列表就是元组 (xx, xx, xx)
print('======== 元组 ======== ')
dimensions = (200,50)
# 访问元素
print(dimensions[0]) 
# dimensions[0]=10 元素不允许修改
for dimension in dimensions: 
    print(dimension)
# 可以赋值整个元组
dimensions = (400,100)
for dimension in dimensions: 
    print(dimension)

# 条件判断 = > >= < <= != ==
car='bmw'
car.lower()=='bmw' # True
car.lower()!='audi' # True
# and / or
age_0=25
age_1=10
age_0 >=21 and age_0 < 50 # True
age_0 < 50 or age_1 > 30
# in / not in
foods=['beef', 'chicken', 'milk']
'milk' in foods # True
if 'salade' not in foods:
    print("no!!")
# if/ elif / else
if age_0 < 4:   
    print('cost 0＄')
elif age_0 < 26:
    print('cost 18＄')
else:
    print('cost 40＄')

# 多个列表判断
available=['mushrooms','olives','green peppers','pepperoni','pineapple', 'extra cheese']
requested=['mushrooms','french fries','extra cheese']
for requested_item in requested:
    if (requested_item in available):
        print(f"adding {requested_item}")
    else:
        print(f"sorry, don't have {requested_item}")
print('finish!')

# 字典
# 定义：一系列键值对，值可以是任意python对象 {key: value}
person= {'color': 'yellow', 'money': '10000',}
# 访问key的值
print(person['money'])
point_value = person.get('point', 'No point value assigned') # ✔推荐，若指定key不存在情况可以报错
print(point_value)
# 修改
person['color']='green'
# 添加键值对
person['name']='yaya'
person['point']='10000'
print(person)
# 删除键值对
del person['color']
print(person)
# 遍历key+value
for key, value in person.items():
    print(f"key: {key} value: {value}")
# 遍历keys
for key in person.keys(): 
    print(key.title())
# keys()可忽略
for key in sorted(person):
    print(key.title())
# 遍历values
# 为剔除重复项，可使用集合(set)。
for key in set(person.values()):
    print(key)

# 集合
# 定义：集合中的每个元素都必须是独一无二的，只有value， {xx, xx, xx}

# 字典列表
alien_0={'color':'green', 'points': 5}
alien_1={'color':'yellow', 'points': 10}
alien_2={'color':'red', 'points': 20}
aliens=[alien_0, alien_2, alien_2] # 列表

# 字典字典
users={
    "yaya":{
        'first': 'xu',
        'last': 'yaya'
    },
    "lala":{
        'first': 'wu',
        'last': 'lala'
    }
}