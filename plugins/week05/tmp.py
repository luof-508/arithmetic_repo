import random


def sort(iterable, key=lambda a, b, reverse: a > b if reverse else a<b):
    n = len(iterable)
    it = iterable[:]
    for i in range(n-1):
        index = i
        for j in range(i+1, n):
            if key(it[j], it[index], False):
                index = j
        if index == i:
            continue
        else:
            it[index], it[i] = it[i], it[index]
    return it


lst = [0] * 20
for k in range(20):
    lst[k] = random.randint(1, 100)
print(lst)
print(sort(lst))
print(sort(lst))

