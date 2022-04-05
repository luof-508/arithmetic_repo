num=int(input('Enter a number:'))
sep=num//2
count=0
for i in range(1,num+1,2):
    print('\t'*(sep-count),' *\t '*i)
    count+=1
if num % 2 !=0:
    for i in range(num-2,0,-2):
        print('\t'*(sep+2-count),' *\t '*i)
        count-=1
else:
    for i in range(num-3,0,-2):
        print('\t'*(sep+2-count),' *\t '*i)
        count-=1


num=int(input('Enter a number>>>'))
if num % 2 == 0:
    count=num//2-1
    for i in range(1,num,2):
        print(' \t' * count + '*\t'*i)
        count-=1
    count=1
    for j in range(num-3,0,-2):
        print(' \t'*count + '*\t'*j)
        count+=1
else:
    count=num//2
    for i in range(1,num+1,2):
        print(' ' * count + '*'*i)
        count-=1
    count=1
    for j in range(num-2,0,-2):
        print(' '*count + '*'*j)
        count+=1



for i in range(-3,4):
    if i <0:
        prespace=-i
    else:
        prespace=i
    print(' '*prespace + '*'*(7-2*prespace))


for i in range(3,-4,-1):
    if i > 0:
        perspace = i
        print(' '* perspace + '*'*(4-perspace))
    elif i == 0:
        perspace = 0
        print('*'*7)
    else:
        perspace = -i
        print(' '* 3 + '*'*(4-perspace))
