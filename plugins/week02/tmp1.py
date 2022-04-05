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
print(m, n, lst1)

for i in range(n):
    flag = i
    for j in range(3):
        lst2.append(lst1[flag])
        flag+=n
    lst3.append(lst2)
    lst2=[]

print(lst3)
