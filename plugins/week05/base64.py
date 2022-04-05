import string
import math
import sys


def base64(key):
    """
    Return the base64.encode
    :param key: int
    :return: str
    """
    base = string.ascii_uppercase + string.ascii_lowercase + string.digits + '+/'
    dic = {}
    for i in range(64):
        dic[i] = base[i]
    return dic[key]


def base64_encodes(src):
    """
    Trans str to 4 * 6bit and return base64_index and base64_encode
    :param src: sub strings
    :return: list
    """
    sub_numbers = math.ceil(len(src) / 3)
    base64_index_encode = []
    cur = 0
    for i in range(sub_numbers):
        sub_lst = src[cur:cur+3]
        if len(sub_lst) < 3:
            sub_01 = ''.join(['0' + bin(ord(s))[2:] for s in sub_lst]) + '0' * 8 * (3 - len(sub_lst))
        else:
            sub_01 = ''.join(['0' + bin(ord(s))[2:] for s in sub_lst])
        tmp = 0
        for i in range(4):
            base64_index = int('0b' + sub_01[tmp:6+tmp], 2)
            base64_encode = base64(base64_index)
            base64_index_encode.append((base64_index, base64_encode))
            tmp += 6
    return base64_index_encode


while True:
    try:
        strings = sys.stdin.readline().strip()
        if not strings:
            break
        re = base64_encodes(strings)
        print(re)
    except:
        break
