num=int(input('enter a number:'))
val=num
if num>=100000 or num<=0:
    print('you must enter a number which is more than 0 and less than 100000.')
elif num>=1000:
    if num >= 10000:
        print(5)
    else:
        print(4)
elif num >=100:
    print(3)
elif num >=10:
    print(2)
else:
    print(1)
##
count=0
while val:
    print(val%10)
    val=val//10
    count+=1
else:
    print(count)

val=123
count=3
pre=0
for i in range(count,0,-1):
    cur=val//(10**(i-1))
    print(cur-pre*10)
    pre=cur
