import random

d = {}
lst = [0]*100
for _ in range(100):
    k = random.randint(-1000,1000)
    if not d.get(k):
        d[k] = 1
    d[k] += 1
print(d)
length = len(d)
lst = [0]*length
count = 0
for item in d.items():
    lst[count] = item
    count += 1
print(lst)

for i in range(0, length):
    index_min = i
    index_max = length-i-1
    for j in range(i+1, length-i):
        if lst[j][0] < lst[index_min][0]:
            index_min = j
        if lst[j][0] > lst[index_max][0]:
            index_max = j
    if index_min != i:
        lst[i], lst[index_min] = lst[index_min], lst[i]
        if index_max == i:
            index_max = index_min
    if index_max != length-i-1:
        lst[length-i-1], lst[index_max] = lst[index_max], lst[length-i-1]
print(lst)

# 效率
import random
from collections import OrderedDict

d = {}
for _ in range(100):
    k = random.randint(-1000,1000)
    if not d.get(k):
        d[k] = 1
    d[k] += 1
print(d)
lst = []
for k in d.keys():
    lst.append(k)
lst = sorted(lst)
print(lst)

dict_descending = OrderedDict()
for k in lst:
    dict_descending[k] = d[k]
print(dict_descending)
