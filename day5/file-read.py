from pathlib import Path

path = Path('files/pi_digits.txt')
contents = path.read_text()
# 删除文件末尾的空字符串
contents = contents.rstrip()

# 访问文件内容
print(contents)

# 访问文件各行
lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.lstrip()
print(pi_string)