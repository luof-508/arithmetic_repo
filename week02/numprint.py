##方法1
num = input("Enter a number>>").strip().lstrip('0')
print('length:{}'.format(len(num)))
cur = ' '
total_count = 0
for i in num:
    if cur == i:
        print("{0}\'s repeat = {1}.".format(i, num_count))
    else:
        print("{0}\'s repeat = {1}.".format(i,num.count(i)))
        cur = i
        num_count = num.count(i)
        total_count += num.count(i)
print('total_count:{}'.format(total_count))

lst = list(num)
lst.reverse()
print(lst)

n = len(num)
for j in range(n,0,-1):
    print("{} ".format(num[j-1]),end='')


##方法二
num = input('Enter a interger number>>>').strip().lstrip('0')
while not num.isdigit():
    print('bad number.')
    num = input('Enter a interger number>>>').strip().lstrip('0')
    continue

grid = [0]*10
for i in range(10):
    grid[i] = num.count(str(i))
for j in range(10):
    if grid[j]:
        print("{0}\'s repeat = {0}.".format(j,))

n = len(num)
for j in range(n,0,-1):
    print("{} ".format(num[j-1]),end='')
