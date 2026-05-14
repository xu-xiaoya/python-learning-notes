# Python Learning Notes

这是一个按天记录的 Python 基础练习项目，目标是把“语法点 + 小例子 + 自己的理解”逐步积累下来，方便后续复习。

## 当前结构

```text
python/
|- day1.py
|- day1_test.py
|- day2.py
|- day3.py
|- day3_import.py
|- day4/
|  |- __init__.py
|  |- __main__.py
|  |- car.py
|  |- demo.py
|  |- dog.py
|  `- electric_car.py
|- day4_import.py
|- day5/
|  |- pi_string.py
|  |- remember_me.py
|  |- write_name.py
|  `- files/
|     |- name.txt
|     |- pi_million_digits.txt
|     `- username.json
|- day6/
|  |- name_function.py
|  `- test_name.py
`- README.md
```

## 学习内容

### Day 1

基础数据类型和常见操作：

- 字符串
- 数字
- 列表
- 切片
- 元组
- 字典
- 集合

### Day 2

流程控制相关内容：

- `if` 条件判断
- `for` 循环和 `range()`
- `while` 循环
- `input()`
- 列表处理练习

### Day 3

函数与模块：

- `def`
- 默认参数
- 位置参数和关键字参数
- `*args`
- 模块导入

### Day 4

面向对象基础：

- 类和对象
- 属性读写
- 继承
- 方法重写
- 组合

### Day 5

文件与异常处理入门：

- 用 `Path` 读取和写入文件
- 处理百万位圆周率文本
- 使用 `json` 保存用户名
- 理解相对路径和脚本路径

### Day 6

测试基础：

- 编写函数 `get_formatted_name()`
- 使用 `pytest` 写简单单元测试
- 通过断言验证函数输出

## 如何运行

运行

```bash
python xx.py
```

## pytest 说明

如果终端里直接输入 `pytest` 提示“无法识别”，通常不是没安装，而是 `pytest.exe` 没有加入系统的 `Path`。

这种情况下，优先使用下面这条命令：

```bash
python -m pytest day6/test_name.py
```

## 后续建议

- 保持“一天一个主题”的结构，方便回顾
- 练习文件读写时，尽量使用 `Path(__file__).parent` 处理路径
- 写测试时，优先用 `python -m pytest`
- 后面内容变多后，可以再拆分成 `notes/`、`examples/`、`exercises/`
