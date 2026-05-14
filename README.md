# Python Learning Notes

这是我的 Python 学习仓库。

目前 `day1-6 'base'` 这一部分是基础阶段，主要用来系统练习 Python 基础语法、文件操作、面向对象和测试。后面继续学习时，会逐步加入项目练习，把前面的基础知识真正用起来。

## 当前结构

```text
python/
|- day1-6 'base'/
`- README.md
```

## 学习阶段

### 第一阶段：基础

`day1-6 'base'` 是基础内容，按主题逐步练习：

- Day 1: 基础数据类型和常见操作
- Day 2: 条件判断、循环、输入与列表处理
- Day 3: 函数、参数、模块导入
- Day 4: 类、对象、继承、组合
- Day 5: 文件读写、`Path`、`json`
- Day 6: `pytest` 单元测试基础

### 第二阶段：项目

后面的学习会逐步进入项目练习，

## 如何运行

如果当前目录在仓库根目录，可以这样运行基础阶段的代码：

```bash
python "day1-6 'base'/day1.py"
python -m pytest "day1-6 'base'/day6/test_name.py"
```

也可以先进入基础目录再运行：

```bash
cd "day1-6 'base'"
python day4_import.py
python -m pytest day6/test_name.py
```

## pytest 说明

如果终端里直接输入 `pytest` 提示“无法识别”，通常不是没安装，而是 `pytest.exe` 没有加入系统环境变量 `Path`。

这种情况下，优先使用：

```bash
python -m pytest day6/test_name.py
```
