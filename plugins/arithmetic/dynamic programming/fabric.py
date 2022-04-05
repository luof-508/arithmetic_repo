# 穷举算法：最大、最小、最重、最长；优化方法
# 高效的穷举——数据结构达到高效
# # 递归 + 记忆 + 猜测---dp（）dynamic programming
# 猜测构造，记忆实现 --递归
# fibrec
# def fib(n):
#     if n <= 1:
#         f = n
#     else:
#         f = fib(n-1) + fib(n-2)
#     return f
# memo = {}
# def fib(n):
#     if memo.get(n):
#         return memo.get(n)
#     if n <= 1:
#         f = n
#         memo[n] = f
#     else:
#         f = fib(n-1) +fib(n-2)
#         memo[n] = fib(n-1) +fib(n-2)
#     return f
# print(fib(35))


# def fib(n, pre=0, cur=1):
#     pre, cur = cur, pre+cur
#     n -= 1
#     if n > 1:
#         return fib(n, pre, cur)
#     return cur
# print(fib(35))


def fib(n, dic=None):
    if not dic:
        dic = {}
    for i in range(n+1):
        if i <= 1:
            dic[i] = i
        else:
            dic[i] = dic[i-1] + dic[i-2]
    return dic[n]


print(fib(35))
