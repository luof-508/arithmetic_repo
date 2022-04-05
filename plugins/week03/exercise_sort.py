####冒泡法排序
import random

lst = []
num = int(input('Enter the sequence length:'))
for _ in range(num):
    lst.append(random.randrange(1, 21))
print('Original list>>>{}'.format(lst))

swap_times = 0
for i in range(num):
    flag = False
    for j in range(num-1-i):
        if lst[j] > lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]
            swap_times += 1
            flag = True
    if not flag:
        break
print('Ascending order>>>{}\nSwap_times = {}'.format(lst,swap_times))


####选择排序法排序
import random

lst = []
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# lst = [9, 8, 7, 6, 5, 4, 3, 2, 1]
# lst = [7, 8, 4, 9, 2, 6, 3, 1, 5]
num = int(input('Enter the sequence length:'))
for _ in range(num):
    lst.append(random.randrange(1, 21))
print('Original list>>>{}'.format(lst))

compare_times = 0
swap_times = 0
for i in range(num):
    original_index = i
    for j in range(i+1,num):
        if lst[j] > lst[original_index]:
            original_index = j
            compare_times += 1
    if original_index != i:
        lst[i], lst[original_index] = lst[original_index], lst[i]
        swap_times += 1
print('Descending order>>>{}\nCompare_times = {}\nSwap_times = {}'.format(lst,compare_times,swap_times))

#### 选择排序法排序优化--极大极小值同时寻找
import random, math

lst = []
num = int(input('Enter the sequence length:'))
for _ in range(num):
    lst.append(random.randrange(1, 51))
lst = [1, 7, 8, 4, 9, 2, 6, 3, 11, 5]
print('Original list>>>{}'.format(lst))

num = len(lst)
compare_times = 0
swap_times = 0
front =[]
for i in range(math.ceil(num/2)):
    max_index = i
    min_index = -1-i
    min_original = min_index
    for j in range(i+1, num-i):
        if lst[j] > lst[max_index]:
            max_index = j
            compare_times += 1
        if lst[-1-j] < lst[min_index]:
            min_index = -1-j
            compare_times += 1
    if max_index != i:
        lst[i], lst[max_index] = lst[max_index], lst[i]
        swap_times += 1
        if min_index == i or min_index + num == i:    # 判断最小值索引是否正好在最大值索引的初始位置，即i位置。此时最小值索引被交换到最大值索引位置。
            min_index = max_index
    if min_original != min_index:
        lst[-1-i], lst[min_index] = lst[min_index], lst[-1-i]
        swap_times += 1
print('Descending order>>>{}\nCompare_times = {}\nSwap_times = {}'.format(lst,compare_times,swap_times))

#### 选择排序法排序优化--极大极小值同时寻找 ,判断元素相等情况
#### 选择排序法排序
import random, math

lst = []
num = int(input('Enter the sequence length:'))
for _ in range(num):
    lst.append(random.randrange(1, 51))
# lst = [1, 7, 8, 4, 9, 2, 6, 3, 11, 5]
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# lst = [9, 8, 7, 6, 5, 4, 3, 2, 1]
lst = [1, 1, 1, 1, 1, 1, 1, 1, 1, 2]
print('Original list>>>{}'.format(lst))

num = len(lst)
compare_times = 0
swap_times = 0
for i in range(math.ceil(num/2)):
    max_index = i
    min_index = -1-i
    min_original = min_index
    for j in range(i+1, num-i):
        if lst[j] > lst[max_index]:
            max_index = j
            compare_times += 1
        if lst[-1-j] < lst[min_index]:
            min_index = -1-j
            compare_times += 1
    if lst[max_index] == lst[min_index]:              # 判断元素相等情况
        break
    if max_index != i:
        lst[i], lst[max_index] = lst[max_index], lst[i]
        swap_times += 1
        if min_index == i or min_index + num == i:    # 判断最小值索引是否正好在最大值索引的初始位置，即i位置。此时最小值索引被交换到最大值索引位置。
            min_index = max_index
    if min_original != min_index:
        lst[-1-i], lst[min_index] = lst[min_index], lst[-1-i]
        swap_times += 1
print('Descending order>>>{}\nCompare_times = {}\nSwap_times = {}'.format(lst,compare_times,swap_times))
