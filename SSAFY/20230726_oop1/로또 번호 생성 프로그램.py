import random

# lotto_nums = []
# while len(lotto_nums) < 6:
#     a = random.randint(1,45)
#     if a in lotto_nums:
#         continue
#     lotto_nums.append(a)
# lotto_nums.sort()
# print(lotto_nums)


# 로또 번호 만드는 애가 있어야 되겠네?
# 로또 번호 정렬하는 애도 있어야 되겠네?

class LottoNumverMaker:
    def __init__(self):
        self.lotto_nums = []

    def create_number(self):
        while len(self.lotto_nums) < 6:
            a = random.randint(1,45)
            if a in self.lotto_nums:
                continue
            self.lotto_nums.append(a)
        pass

    def lotto_sort(self):
        self.lotto_nums.sort()
        pass

LM = LottoNumverMaker()

LM.create_number()
LM.lotto_sort()
print(LM.lotto_nums)