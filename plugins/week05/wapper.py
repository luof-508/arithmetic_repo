# #   无参数装饰器
# import datetime
# import time
#
#
# def copy_properities(src, dst):
#     # def copy_src(dst):
#     dst.__name__ = src.__name__
#     dst.__qualname__ = src.__qualname__
#     dst.__doc__ = src.__doc__
#
#
# def log_dir(fn):
#     """
#     This is a wrapper.
#     :param fn: function
#     :return: wrapper function
#     """
#     def wrapper(x, y, *args, **kwargs):
#         """
#         Improve add function
#         """
#         print('before')
#         start = datetime.datetime.now()
#         re = fn(x, y, *args, **kwargs)
#         dalta = (datetime.datetime.now() - start).total_seconds()
#         print('too slow') if dalta > 5 else print('so fast')
#         print('after')
#         return re
#     copy_properities(fn, wrapper)    # 将原add函数特殊属性复制过来，
#     return wrapper
#
#
# @log_dir  # 等价于在add函数后进行 add = log_dir(add)调用
# def add(x, y, *args, **kwargs):
#     """
#     Calculate the sum of arguments
#
#     :param x: int
#     :param y: int
#     :param args: int
#     :param kwargs: int
#     :return:
#     """
#     re = x + y + sum(args) +sum(kwargs.values())
#     time.sleep(2)
#     return re
#
#
# # add = log_dir(add) --> add = wrapper --> 调用wrapper函数,此处原add函数被重新定义，然而原add函数
# # 在第一步被传入闭包里面被作为局部变量被保留下来，且外部环境不可见。--> 执行wrapper函数调用。
# print(add(4, 5, 6, 7, 8))
# print(add.__name__, add.__qualname__, add.__doc__)

# 无参装饰器
# 是一个函数
# 函数作为形参
# 返回值必须是一个函数
# 可使用@functionname，简化调用
import datetime
import time


def logger(func):
    def wrapper(*args, **kwargs):
        print("args = {}, kwargs = {}".format(args, kwargs))
        start = datetime.datetime.now()
        ret = func(*args, **kwargs)
        end = datetime.datetime.now() - start
        print("function {} took {}s.".format(func.__name__, end.total_seconds()))
        return ret
    return wrapper


@logger
def add(*args, **kwargs):
    print("====call add====")
    time.sleep(2)
    return sum(args) + sum(kwargs.values())


print(add(1, 2, 3, x=4, y=5))
