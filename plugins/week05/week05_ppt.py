import random


def comp(a, b):
    return a < b


def sort(iterable, key=lambda a, b: a < b, reverse=False):
    lst = []
    for x in iterable:
        for i, y in enumerate(lst):
            if key(x, y):
                lst.insert(i, x)
                break
        else:
            lst.append(x)
    return lst


test_lst = [random.randint(10, 30) for i in range(8)]
print(test_lst)
sorted_lst = sort(test_lst, reverse=True)
print(sorted_lst)
print(sorted(test_lst, key=lambda x: -x))

dic = [(9, 3), (2, 4)]
print(sorted(dic, key=lambda x: x[0]))

simple = [26, 20, 11, 23, 21, 23, 15, 23]
for i in filter(lambda x: x - 15 > 0, simple):
    print(i)

print(list(map(lambda x, y: isinstance(x, type(y)), simple, dic)))
print(type((9,)))

print(dict(map(lambda x: (x % 5, x), range(500))))
