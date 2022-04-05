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
