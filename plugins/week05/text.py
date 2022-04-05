# s = input('>>>')
#
#
# def log_dir(src):
#     lst = ['s1', 's2', 's3']
#     if src in lst:
#         def dst(x):
#             re = src(x)
#             return re
#     else:
#         def dst(x, y):
#             return x + y
#     return dst
#
#
# @log_dir(s)
# def func():
#     return


def counter(base):
    def wrapper(*args, **kwargs):
        print("before")
        res = base(*args, **kwargs)
        print("after")
        return res
    return wrapper


@counter  # add = counter(add)
def add(x, y, *args, z, **kwargs):
    return x + y + z + sum(args) + sum(kwargs.values())


print(add(1, 2, z=5, a=4))
