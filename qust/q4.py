import random

str = "asdfghjklmnbvcxz"
s = ''

for i in range(1,1000):
    a = random.choice(str)
    s += a

s1 = set(s)

zd = {}
for i in s1:
    zd[i] = s.count(i)

print(zd)