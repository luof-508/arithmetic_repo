########打印每一位数及其重复次数
import random

dig = int(input('Enter the digits of number>>>'))
num = str(random.randrange(10**(dig-1), 10**dig))
print('num = {}'.format(num))

dic = {}
for key in num:
    if not dic.get(key):
        dic[key] = 1
    else:
        dic[key] += 1
### if语句优化一
    if key not in dic:   # if key not in dic.key():
        dic[key] = 0
    dic[key] += 1
### if 语句优化二
    dic[key] = dic.get(key,0) + 1

print('The number and repetitions>>>')
for numbers, repeat in dic.items():
    print(numbers, repeat)

##### 数字统计， 随机产生100个数，统计重复数字及升序打印
###使用字典
import random
from collections import OrderedDict

dic = {}
for _ in range(100):
    num = int(random.randrange(-1000, 1001))
    if not dic.get(num):
        dic[num] = 1
    else:
        dic[num] += 1
print('Repetition statistic of number by dict>>>{}'.format(dic))

lst = []
for key in dic.keys():
    lst.append(key)
#### 提高效率方法：l = len(dic); lst = [0] * l; for key in dic.keys():   lst[key] = key
print('Random arrangement of key>>>{}'.format(lst))

length = len(lst)
for i in range(length):
    min_index = i
    for j in range(i+1, length):
        if lst[j] < lst[min_index]:
            min_index = j
    if i == min_index:
        continue
    else:
        lst[i], lst[min_index] = lst[min_index], lst[i]
print('The ascending sort of Key>>>{}'.format(lst))

dic_ascending = OrderedDict()
for key in lst:
    dic_ascending[key] = dic[key]
print('The ascending arrangement of number and the repetition of number>>>{}'.format(dic_ascending))




######a-z的两个随机组合字符串排序及重复统计
###使用字典

import random
from collections import OrderedDict

string = 'abcdefghijklmnopqrstuvwxyz'
dic = {}
for _ in range(100):
    str_rand = random.choice(string) + random.choice(string)
    if not dic.get(str_rand):
        dic[str_rand] = 1
    else:
        dic[str_rand] += 1
print('Random arrangement of string and repetition statistic>>>{}'.format(dic))


lst = []
for key in dic.keys():
    lst.append(key)
print('The random arrangement of key>>>{}'.format(lst))

length = len(lst)
d_descending = OrderedDict()
for i in range(length):
    max_lst = i
    for j in range(i, length):
        if lst[j] > lst[max_lst]:
            max_lst = j
    if max_lst == i:
        d_descending[lst[i]] = dic[lst[i]]
        continue
    else:
        lst[i], lst[max_lst] = lst[max_lst], lst[i]
        d_descending[lst[i]] = dic[lst[i]]
# for key in lst:
#    d_descending[key] = dic[key]
print('Descending arrangement of string and repetition statistic>>>{}'.format(d_descending))

###方法二 使用sorted
import string
import random
dic = {}
for i in range(100):
    key = random.choice(string.ascii_lowercase) + random.choice(string.ascii_lowercase)
    if not dic.get(key):
        dic[key] = 1
    dic[key] += 1
print(dic)

lst = sorted(dic.items(), reverse=True)
print(lst)
