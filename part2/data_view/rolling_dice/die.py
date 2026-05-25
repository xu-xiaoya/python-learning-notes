from random import randint
# 骰子类
class Die:
    def __init__(self, num_sides=6):
        # 默认6面
        self.num_sides = num_sides

    def roll(self):
        return randint(1, self.num_sides)