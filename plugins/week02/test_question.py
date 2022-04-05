####一、 求n阶杨辉三角形
##方法一
n = int(input('Enter the \'n\'>>>'))
triangle = [[1]]
for i in range(2,n+1):
    if i == 2:
        triangle.append([1,1])
    else:
        lst=[1]*i
        for j in range(1,i-1):
            lst[j]=triangle[i-2][j-1]+triangle[i-2][j]
        triangle.append(lst)
print(triangle[n][5])

#### 求杨辉三角形第m行第n个元素
##方法一
m = int(input('Enter the \'row\'>>>'))
k = int(input('Enter the \'column\'>>>'))
while k > m :
    print("Error:\'k\' must less than \'m\'.")
    k = int(input('please enter \'k\' again>>>'))
triangle = [1]
for j in range(2, m+1):
    if j == 2:
        triangle.append(1)
    else:
        lst = [1]*j
        for i in range(1, j-1):
            lst[i] = triangle[i-1]+triangle[i]
        triangle = lst.copy()
print('The number of {} row :{} column is {}.'.format(m,k,triangle[k-1]))


##方法一升级，只计算一半
n = int(input('Enter the \'n\'>>>'))
triangle = [[1]]
for i in range(2,n+1):
    if i == 2:
        triangle.append([1, 1])
    else:
        lst = [1] * i
        for j in range(1,i//2+1):
            lst[j] = triangle[i-2][j-1] + triangle[i-2][j]
            if j < i-j:
                lst[-j-1] = lst[j]
        triangle.append(lst)
print(triangle)

#### 求杨辉三角形第m行第n个元素
##方法一升级，只计算一半
m = int(input('Enter the \'row\'>>>'))
k = int(input('Enter the \'column\'>>>'))
while k > m :
    print("Error:\'k\' must less than \'m\'.")
    k = int(input('please enter \'k\' again>>>'))
triangle = [1]
for i in range(2,m+1):
    if i == 2:
        triangle.append(1)
    else:
        lst = [1] * i
        for j in range(1,i//2+1):
            lst[j] = triangle[j-1] + triangle[j]
            if j < i-j:
                lst[-j-1] = lst[j]
        triangle=lst.copy()
print(triangle[k-1])




#### 求杨辉三角形
##方法二
n = int(input('Enter the \'n\'>>>'))
triangle = [[1]]
mid=[1]
for i in range(2, n+1):
    mid.append(0)
    lst=[1]*i
    for j in range(1,i):
        lst[j] = mid[j-1] + mid[j]
    mid=lst.copy()
    triangle.append(lst)
print(triangle)

#### 求杨辉三角形第m行第n个元素
##方法二
import copy
m = int(input('Enter the \'row\'>>>'))
k = int(input('Enter the \'column\'>>>'))
while k > m :
    print("Error:\'k\' must less than \'m\'.")
    k = int(input('please enter \'k\' again>>>'))

triangle = [1]
for i in range(2,m+1):
    triangle.append(0)
    lst=[1]*i
    for j in range(i):
        lst[j]=triangle[j-1]+triangle[j]
    triangle=lst.copy()
print(triangle[k-1])


#### 求n阶杨辉三角形
###方法三 加0计算
n = int(input('Enter the \'n\'>>>'))
triangle = [[1]]
pre = [1]
for i in range(2,n+1):
    pre.append(0)
    lst = []
    for j in range(i):
        lst.append(pre[j-1] + pre[j])
    triangle.append(lst)
    pre=lst.copy()
print(triangle)

#### 求杨辉三角形第m行第n个元素
##方法三
m = int(input('Enter the \'row\'>>>'))
k = int(input('Enter the \'column\'>>>'))
while k > m :
    print("Error:\'k\' must less than \'m\'.")
    k = int(input('please enter \'k\' again>>>'))
triangle = [1]


#####二、求方阵的转置矩阵。
lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
n = len(lst)
count_swap = 0
for i in range(n):
    for j in range(i):
        if i == j:
            continue
        mid=lst[i][j]
        lst[i][j] = lst[j][i]
        lst[j][i] = mid
        count_swap += 1
print(lst)
print(count_swap)

#####三、求矩阵的转置矩阵。
lst0 = [[1, 2, 3], [4, 5, 6],[2, 4, 6]]
lst1 = []
lst2 = []
lst3 = []
m = len(lst0)
n = len(lst0[0])
for i in range(m):
    for j in range(n):
        lst1.append(lst0[i][j])
k = len(lst1)

for i in range(n):
    flag = i
    for j in range(3):
        lst2.append(lst1[flag])
        flag+=n
    lst3.append(lst2)
    lst2=[]
print(lst3)
