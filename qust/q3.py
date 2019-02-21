import random

list = []

for i in range(0,21):
    a = random.randint(0,10)
    list.append(a)

list[::2] = sorted(list[::2],reverse=True)
print(list)