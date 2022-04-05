def max_subarray_sum(lst):
    n = len(lst) + 1
    subarray_sum_lst = []
    for i in range(n):
        subarray_sum_lst.append([0] * n)
        for j in range(n):
            if not i:
                if not j:
                    subarray_sum_lst[i][j] = min(lst)
                else:
                    subarray_sum_lst[i][j] = max(lst[j-1], lst[j-2])         # 第一行相当于sorted(lst)
            else:
                subarray_sum_lst[i][j] = max(subarray_sum_lst[i][j-1], subarray_sum_lst[i-1][j]+lst[j-1])
    return subarray_sum_lst


A = [-9, 1, 5, 4, -3]
sum_array = max_subarray_sum(A)
print(A)
for l in sum_array:
    print(l)

