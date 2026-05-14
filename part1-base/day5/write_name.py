from pathlib import Path

name = input('please enter your name: ')

path = Path(__file__).parent / 'files' / 'name.txt'

try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f"Sorry, the file {path} does not exist.")
    # pass
    
path.write_text(name)