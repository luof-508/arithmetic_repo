import datetime
import time


def pop(dicts):
    delta = datetime.timedelta(minutes=1)
    data_time = (datetime.datetime.now() - delta).timestamp()
    for k, v in dicts.items():
        _, time_record = v
        if float(time_record) < data_time:
            dicts.pop(k)
    return dicts


def cache(fn, dic=None):
    if not dic:
        dic = {}

    def wrapper(*args, **kwargs):
        tup = ('sep',)
        if args:
            tup = args + tup
        if kwargs:
            tup += tuple(sorted(kwargs.values()))
        if dic.get(tup):
            return dic.get(tup)[0]
        res = fn(*args, **kwargs)
        delta = datetime.datetime.now().timestamp()
        _res = str(res), str(delta)
        dic[tup] = _res
        pop(dic)
        return res
    return wrapper


@cache
def add(*args, **kwargs):
    time.sleep(2)
    re = sum(args) + sum(kwargs.values())
    return re


print(add(4, 5))
