#1prime ,效率比较。
import math
import datetime
num=10000
primelist=[2]
count=0
start=datetime.datetime.now()
for i in range(3,num+1):
    for j in range(2,math.ceil(i)):
        count+=1
        if i % j == 0:
            break
    else:
        primelist.append(i)
print(primelist)
print(len(primelist))
print(count)
end=datetime.datetime.now()
print((end-start).total_seconds())


import math
import datetime
num=10000
primelist=[]
count=0
flag=False
start=datetime.datetime.now()
for i in range(2,num):
    for j in primelist:
        count+=1
        if i % j == 0:
            flag=True
            break
        if j >= math.ceil(i**0.5):
            flag=False
            break
    if not flag:
        primelist.append(i)
print(primelist)
print(len(primelist))
print(count)
end=datetime.datetime.now()
print((end-start).total_seconds())
