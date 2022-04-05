lst=[]
for i in range(3):
   num=int(input('Enter a number>>>'))
   lst.append(num)
if lst[0] <= lst[1]:
    if lst[0] <= lst[2]:
        if lst[1] <= lst[2]:
            print(lst[0],lst[1],lst[2])
        else:
            print(lst[0],lst[2],lst[1])
    else:
        print(lst[2],lst[0],lst[1])
else:
    if lst[1] <= lst[2]:
        if lst[0] <= lst[2]:
            print(lst[1],lst[0],lst[2])
        else:
            print(lst[1],lst[2],lst[0])
    else:
        print(lst[2],lst[1],lst[0])

print(max(lst))


a=int(input('Enter a number>>>'))
b=int(input('Enter a number>>>'))
c=int(input('Enter a number>>>'))
cur=max(a,b,c)
if cur == a:
    print(b,c,a) if c > b else print(c,b,a)
elif cur == b:
    print(c,a,b) if a > c else print(a,c,b)
else:
    print(b,a,c) if a > b else print(a,b,c)


lst=[]
row=[]
for i in range(3):
    num=int(input('{}: '.format(0)))
    lst.append(num)
while True:
    cur=min(lst)
    lst.remove(cur)
    row.append(cur)
    if len(lst) == 1:
        break
row.append(lst[0])
print(row)



lst=[]
for i in range(3):
   num=int(input('Enter a number>>>'))
   lst.append(num)
lst.sort()
print(lst)
