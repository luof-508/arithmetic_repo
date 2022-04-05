# 带参装饰器，将记录判断功能提出出来
import datetime
import time

def copy_properities(src):
    def copy_src(dst):
        dst.__name__ = src.__name__
        dst.__qualname__ = src.__qualname__
        dst.__doc__ = src.__doc__
        return dst
    return copy_src


def _logger(duration, func=lambda name, duration: print('{} took {}s'.format(name, duration))):
    def logger(fn):
        """
        This is a wrapper.
        :param fn: function
        :return: wrapper function
        """
        @copy_properities(fn)
        def wrapper(x, y, *args, **kwargs):
            """
            Improve add function
            """
            print('before')
            start = datetime.datetime.now()
            re = fn(x, y, *args, **kwargs)
            dalta = (datetime.datetime.now() - start).total_seconds()
            if dalta > duration:
                func(fn.__name__, duration)# print('too slow')
            print('after')
            return re
        # @copy_properities(fn) 等价于在此处执行：wrapper = copy_properities(wrapper)
        return wrapper
    return logger


@_logger(2)  # 等价于在add函数后进行 add = log_dir(add)调用，
#              log_dir(add)返回的是wrapper,所以打印add.__name__返回的是wrapper的特色属性
def add(x, y, *args, **kwargs):
    """
    Calculate the sum of arguments

    :param x: int
    :param y: int
    :param args: int
    :param kwargs: int
    :return:
    """
    re = x + y + sum(args) +sum(kwargs.values())
    time.sleep(2)
    return re


print(add(4, 5, 6, 7, 8))
print(add.__name__, add.__qualname__, add.__doc__)
