import random
def extrema(x, y, *args):
    print('max={}'.format(max(x, y, *args)))
    print('min={}'.format(min(x, y, *args)))
print(*(extrema(*[random.randint(0, 100) for _ in range(10)])))

#### 打印上三角函数
### 笨方法
def print_n(n):
    for i in range(1, n+1):
        for j in range(n, 0, -1):
            if i <j:
                # for i in range(len(str(n)), 0)
                #    print('{:<i+2}'.format(''),end='')
                if j >= 10:
                    print('{:<4}'.format(''), end='')
                else:
                    print('{:<3}'.format(''), end='')
            else:
                if j >= 10:
                    print('{:<4}'.format(j), end='')
                else:
                    print('{:<3}'.format(j), end='')
        print()
### 终极方法
def show(n):
    tail = ' '.join([str(i) for i in range(n, 0, -1)])
    width = len(tail)
    for i in range(1, n):
        print('{0:>{1}}'.format(' '.join([str(j) for j in range(i, 0, -1)]), width))
    print(tail)

#### 打印下三角函数
### 笨方法
def print_n(n):
    for i in range(n):
        for j in range(n, 0, -1):
            if j > n-i:
                if j >= 10:
                    print('{:<4}'.format(''), end='')
                else:
                    print('{:<3}'.format(''), end='')
            else:
                if j >= 10:
                    print('{:<4}'.format(j), end='')
                else:
                    print('{:<3}'.format(j), end='')
        print()
### 终极方法
def show(n):
        tail = ' '.join([str(i) for i in range(n, 0, -1)])
        width = len(tail)
        print(tail)
        for i in range(n-1, 0, -1):
            print('{0:>{1}}'.format(' '.join([str(j) for j in range(i, 0, -1)]), width))
