import random

list = []

for i in range(1,51):
    a = random.randint(-10,10)
    list.append(a)

zlist = []
flist = []

for i in list:
    if i > 0 :
        zlist.append(i)
    else:
        flist.append(i)


print(zlist)
print(flist)