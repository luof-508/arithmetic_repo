num=int(input('Enter a number>>>'))
m=0
n=1
for i in range(num):
    if i == m+n :
        print(i)
        m=n
        n=i
#
m=0
n=1
for i in range(3,102):
        sum=m+n
        m=n
        n=sum
print(sum)
