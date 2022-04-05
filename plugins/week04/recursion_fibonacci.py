"""
递归有深度限制，压栈出栈，反复压栈，容易栈溢出，效率较低
能不要则不用
绝大多少递归都能用循环代替
"""
# 用递归求fibonacci数列
# 递推公式：fn(n) = fn(n-1) + fn(n-2)
import sys
import datetime


def fib_const(n):
    """
    求fibonacci数列第n项的值
    :param n:
    :return:
    """
    pre, cur = 1, 1
    if n <= 2:
        return cur
    for i in range(2, n+1):
        pre, cur = cur, pre + cur
    return cur


def get_fib_list(n):
    fib_lst = []

    def fib(num):
        return 1 if num <= 2 else fib(num-1) + fib(num-2)

    for i in range(1, n+1):
        fib_lst.append(fib(i))
    return fib_lst


def get_fib_list_improve(n, pre=0, cur=1, fib_list=None):
    if not fib_list:
        fib_list = []
    fib_list.append(cur)
    pre, cur = cur, cur + pre
    if n == 1:
        return
    get_fib_list_improve(n-1, pre, cur, fib_list)
    return fib_list


if __name__ == '__main__':
    print(sys.getrecursionlimit())
    now = datetime.datetime.now()
    fib_res = get_fib_list_improve(35)
    after = datetime.datetime.now()
    delta = (after - now).total_seconds()
    print(fib_res)
    print(delta)
    print('-------------------------------')
    fib_bad_res = get_fib_list(35)
    end = datetime.datetime.now()
    delta_ = (end - after).total_seconds()
    print(fib_bad_res)
    print(delta_)


