import random
lst = []
for i in range(10):
    lst.append(random.randrange(1, 20))
print(lst)
counts = 0
duplicate = []
not_repeat =[]
for i in range(21):
    repeat = lst.count(i)
    if repeat > 1:
        counts += 1
        duplicate.append(i)
    if repeat == 1:
        not_repeat.append(i)
print('{} numbers are duplicated creation>>>{}'.format(counts,duplicate))
print('Do not repeat>>>{}'.format(not_repeat))
