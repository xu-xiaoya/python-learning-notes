from pathlib import Path


path = Path('./files/pi_million_digits.txt')

contents = path.read_text()
# 删除文件末尾的空字符串
contents = contents.rstrip()

# 访问文件各行
lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.lstrip()

print(f"{pi_string[:52]}...")
print(len(pi_string))

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")