######用户输入三个数，排序后打印，不同方法
lst=[]
for i in range(3):
    lst.append(int(input('Enter a number:{}: ').format(i)))

if lst[0] >= lst[1]:
    if lst[0] <lst[2]:
        print(lst[1],lst[0],lst[2])
    else:
        if lst[1] >= lst[2]:
            print(lst[2],lst[1],lst[0])
        else:
            print(lst[1],lst[2],lst[0])
else:  #lst[0] < lst[1]
    if lst[0] <lst[2]:
        if lst[1] < lst[2]:
            print(lst[0],lst[1],lst[2])
        else:
            print(lst[0],lst[2],lst[1])
    else:
        print(lst[2],lst[0],lst[1])


lst=[]
for i in range(3):
    lst.append(int(input('Enter a number:{}: ').format(i)))
while True:
    m = min(lst)
    print(m)
    lst.remove(m)
    if len(lst) == 1:
        print(lst[0])
        break


lst=[]
for i in range(3):
    lst.append(int(input('Enter a number:{}: ').format(i)))
lst.sort()
print(lst)

###冒泡法
#lst = []
#for i in range(3):
#    lst.append(int(input('Enter a number:{}: ').format(i)))

lst=range(11)
count = 0
count_swap = 0
n = len(lst)
flag = True
for i in range(n,0,-1):
    flag = False    #减少count次数，提高效率
    for j in range(0,i-1):
        count += 1
        if lst[j] >= lst[j+1]:
            mid = lst[j]
            lst[j] = lst[j+1]
            lst[j+1] = mid
            flag = True
            count_swap += 1
    if not flag:
        break
    cur = lst[j]
print('sort ascend is:{0}. count = {1}. count_swap = {2:<2}'.format(lst,count,count_swap))




#############用户输入一个数，判断几位数及出现的次数，并按个十百千打印。
print('Enter a integer number',end=' ')
while True:
    num = input(">>>")
    if num.isdigit():
        break
    print('Error:you must enter a integer number.')
print('length = {}.'.format(len(num)))

##方法一
counter = [0]*10
for i in num:
    i = int(i)
    if counter[i] == 0:
        counter[i] = num.count(str(i))
print(counter)
for j in range(10):
    if counter[j] != 0:
        print('The times of {} = {}'.format(j,counter[j]))

##方法一
counter = [0]*10
for i in num:
    i = int(i)
    if counter[i] == 0:
        counter[i] = num.count(str(i))
        print('The times of {} = {}'.format(j,counter[j]))

##方法一优化：
counter = [0]*10
for i in range(10):
    counter[i] = num.count(str(i))
    if counter[i] :
        print('The times of {} = {}'.format(i,counter[i]))

##方法二
counter = [0]*10
for i in num:
        counter[int(i)] +=1
print(counter)



m=len(num)
for i in range(m,0,-1):
    print(num[i-1],end=' ')




#######输入5个数字打印数字长度及升序打印
print('Enter 5 number,use \',\' to split.',end=' ')
num = input('>>>').strip().lstrip(' 0')
lst = num.split(',')
while len(lst) < 5:
    print('Error: you must enter 5 number')
    num = input('>>>').strip().lstrip(' 0')
    lst = num.split(',')

##方法一
lst0 = []
for i in range(len(lst)):
    print('length = {}'.format(len(lst[i])))
    lst0.append(int(lst[i]))
lst0.sort()
print(lst0)

##方法二
lst0 = []
for i in lst:
    lst0.append(int(i))
#冒泡法
n = len(lst0)
for i in  range(n):
    flag = False
    for j in range(n-i-1):
        if lst0[j] > lst0[j+1]:
            mid = lst0[j+1]
            lst0[j+1] = lst0[j]
            lst0[j] =mid
            flag = True
    if not flag:
        break
print('sort ascend of lst0 is {}.'.format(lst0))
