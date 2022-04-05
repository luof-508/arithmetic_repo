# direct insertion sort
import random

n = int(input('enter a number>>>'))
lst = [0]*n
for i in range(n):
    lst[i] = random.randint(0, 100)
print('Random sequence>>>{}'.format(lst))

lst = [9, 87, 57, 49, 96, 72, 44, 75, 72, 9, 16, 59]
counter_loop = 0
counter_swap = 0

#  my method..
num = [0] + lst
for i in range(2, n+1):
    counter_loop += 1
    num[0] = num[i]
    j = i - 1
    while num[j] > num[0]:
        num[j+1] = num[j]
        j -= 1
        counter_swap += 1
    num[j+1] = num[0]
_, *new_lst = num
print('Ascending sequence>>>{}'.format(new_lst))
print('loop = {},swap = {}'.format(counter_loop, counter_swap))

# video method
counter_loop = 0
counter_swap = 0
num = [0] + lst
for i in range(2,n+1):
    counter_loop += 1
    num[0] = num[i]
    j = i - 1
    if num[j] > num[0]:
        # num[j+1] = num[j]
        # j -= 1
        # counter_swap += 1
        while num[j] > num[0]:
            num[j+1] = num[j]
            j -= 1
            counter_swap += 1
        num[j+1] = num[0]
_, *new_lst = num
print('Ascending sequence>>>{}'.format(new_lst))
print('loop = {},swap = {}'.format(counter_loop, counter_swap))
