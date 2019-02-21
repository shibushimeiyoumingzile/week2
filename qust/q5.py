s='The column above illustrates apparently' \
  ' the polularity of people ' \
  'doing exercise in a certain year ' \
  'from 2013 to 2018.Based upon the data,' \
  'we can see that python is wonderful. ' \
  'python is wonderful. Python ' \

s1 = s.replace("."," ")
s2 = s1.split(" ")

set = set(s2)
zd = {}
for i in set:
    zd[i] = s.count(i)

zdd = sorted(zd.items(),key=lambda x:x[1])
zddd = dict(zdd)
print(zddd)
