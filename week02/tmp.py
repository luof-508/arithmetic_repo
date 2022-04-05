lst = [[1,2,3],[4,5,6],[7,8,9]]
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
