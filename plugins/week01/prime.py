num=int(input('Enter a number:'))
for i in range(2,num):
    if num % i ==0:
        print('It\'s not a prime number.')
        break


N=int(input('Enter a number>>>'))
print(2)
sum=0
count=0
for num in range(3,N):
    for i in range(2,num):
        if num % i != 0:
            count+=1
    if count == num-2 :


        print(num)
    count=0


#import time
#time_start=time.time()
import datetime
start=datetime.datetime.now()
count=1
print(2)
for i in range(3,10000,2):            #大于等于3的数中排除偶数
    for j in range(3,int(i**0.5)+1,2):    #如果一个数能够分解成两个因数相乘，如果其中一个因素为偶数，那么这个数一定也是偶数，因为偶数与奇数相乘是偶数，与偶数相乘还是偶数.
        if i%j==0:
            break
    else:
        print(i)
        count+=1
#time_end=time.time()
#time_c=time_end-time_start
end=datetime.datetime.now()
time_c=end-start
print('time cost',time_c,'ms')
print('count=' + count)
