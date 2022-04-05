####列表解析式习题
###
lst = [i**2 for i in range(1,11)]
print(lst)

lst = [1, 4, 9, 16, 2, 5, 10, 15]
print(lst)
lst_new = [ lst[i-1]+lst[i] for i in range(1,len(lst))]
print('lst_new = {}'.format(lst_new))


####乘法表
lst = [['{}*{}={:<3}'.format(i, j, i*j) for j in range(1, i+1)] for i in range(1, 10)]
for i in range(len(lst)):
    print(lst[i])
    print()

###方法二：
multiply = '\n'.join([' '.join(['{}*{}={:<3}\t'.format(i, j, i*j) for j in range(1, i+1)]) for i in range(1,10)])
print(multiply)

###方法三
[print('{}*{}={:<4}{}'.format(i, j, i*j, '\t\n' if i == j else '\t'), end='') for i in range(1, 10) for j in range(1, i+1)]



######打印4位数字ID+10位随机string
import random, string

###方法一
alphabet = string.ascii_lowercase
id_alph = [0] * 100
for i in range(1, 100):
    alph = ''
    for j in range(10):
        alph += random.choice(alphabet)
    id_alph[i-1] = '.'.join([str(i).zfill(4), alph])
print(id_alph)

###方法二
import random, string

alphabet = string.ascii_lowercase
lst = ['.'.join([str(i).zfill(4), ''.join([random.choice(alphabet) for j in range(10)])]) for i in range(1,101)]
print(lst)
for l in lst:
    print('{}\n'.format(l,))

###方法三   （灵活运用了格式化字符串占0，以及bytes的编码和解码，以及字母在ASCii码中的位置）
lst = ['{04}.{}'.format(i, ''.join([random.choice(bytes(range(97, 123)).decode()) for _ in range(10)])) for i in range(1, 101)]
print(lst)
