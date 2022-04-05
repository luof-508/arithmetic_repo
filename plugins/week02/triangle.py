num=6
triangle=[[1],[1,1]]
for i in range(2,num):
    cur=[1]
    pre=triangle[i-1]
    for j in range(i-1):
        cur.append(pre[j]+pre[j+1])
    cur.append(1)
    triangle.append(cur)
print(triangle)





num=int(input('Enter a positive number:'))
if num == 1:
    triangle=[[1]]
else:
    triangle=[[1]]
    for i in range(1,num):
        cur=[1]
        pre=triangle[i-1]
        for j in range(i-1):
            cur.append(pre[j]+pre[j+1])
        cur.append(1)
        triangle.append(cur)
print(triangle)


n=int(input('Enter a positive number:'))
#n=6
triangle=[]
for i in range(n):
    row=[1]
    triangle.append(row)
    if i==0:
        continue
    for j in range(i-1):
       triangle[i].append(triangle[i-1][j]+triangle[i-1][j+1])
    triangle[i].append(1)
print(triangle)



num=int(input('Enter a number:'))
n=num+2
triangle=[1]
triangle.insert(0,0)
triangle.insert(2,0)
for i in range(2,n):
    triangle0=[0]*(n-1)
    for j in range(i):
        triangle0[j]=triangle[j]+triangle[j+1]
    triangle=triangle0.copy()
    triangle.insert(0,0)
    triangle.insert(i+1,0)
print(triangle0)


#n=int(input('Enter a number:'))
n=7
triangle=[1]
triangle.insert(0,0)
triangle.insert(2,0)
for i in range(2,n+1):
    triangle0=[0]*(i)
    for j in range(i):
        triangle0[j]=triangle[j]+triangle[j+1]
    triangle=triangle0.copy()
    triangle.insert(0,0)
    triangle.insert(i+1,0)
print(triangle0)



n = 6
oldline = []
newline = [1]
length = 0
print(newline)
for i in range(1, n):
    oldline = newline.copy()
    oldline.append(0) #
    newline.clear()
    offset = 0
    while offset <= i:
        newline.append(oldline[offset-1] + oldline[offset])
        offset += 1
print(newline)


n=6
oldlist=[]
newlist=[1]
length=0
print(newlist)
for i in range(1,n):
    oldlist=newlist.copy()
    oldlist.append(0)
    newlist.clear()
    offset=0
    while offset<=i:
        newlist.append(oldlist[offset-1]+oldlist[offset])
        offset+=1
print(newlist)


n=6
oldlist=[]
newlist=[1]
length=0
print(newlist)
for i in range(1,n):
    oldlist=newlist.copy()
    oldlist.append(0)
    newlist.clear()
    offset=0
    for j in range(i+1):
        newlist.append(oldlist[j-1]+oldlist[j])
print(newlist)


#问题代码，没搞清楚深拷贝
import copy
num=6
pre=[[]]
triangle=[[]]
for i in range(num-1):
    triangle += copy.deepcopy(pre)
for x in range(num):
    if x == 0:
        triangle[0].append(1)
        continue
    else:
        mid=copy.deepcopy(triangle[x-1])
        mid.append(0)
        for j in range(x+1):
            triangle[x].append(mid[j-1]+mid[j])
print(triangle)



triangle = []
n = 6
for i in range(n):
    row = [1]
    for k in range(i):
        if k == i-1:
            row.append(1)
        else:
            row.append(0)
    triangle.append(row)
    if i == 0:
        continue
    for j in range(1,i//2+1):
        val = triangle[i - 1][ j-1] + triangle[i - 1][ j]
        row[ j] = val
        if j != i - j:
            row[-j-1] = val
print(triangle)



n=3
triangle=[]
for i in range(n):
    row=[1]*(i+1)
    triangle.append(row)
    if i==0:
        continue
    for k in range(1,i//2+1):
        val=triangle[i-1][k-1]+triangle[i-1][k]
        row[k]=val
        if k != i - k:
            row[-k-1] = val
print(triangle)
