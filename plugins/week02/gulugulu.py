#lis=[]
#for i in range(i):
#    num=int(input('{}: '.format(i)))
#    lis.append(num)
#num=len(lis)

import random
import datetime
num=int(input('Enter a number>>>'))
lst=[]
start=datetime.datetime.now()
for i in range(num):
    lst.append(random.randint(0,1000))
print(lst)
count=0
count_swap=0
for j in range(num-1,0,-1):
    count+=1
    flag=True
    for k in range(j):
        tmp=0
        if lst[k] < lst[k+1] :
            tmp = lst[k]
            lst[k] = lst[k+1]
            lst[k+1] = tmp
            count_swap+=1
            flag=False
    if flag :
        break
end=datetime.datetime.now()
tt=(end-start).total_seconds()
print(lst)
print(count,count_swap,tt)
