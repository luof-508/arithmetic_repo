"""
求公共子串
"""
import random
import re
import string
import logging


def _logger():
    res_logger = logging.getLogger(__name__)
    res_logger.setLevel(level=logging.INFO)
    fm = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch = logging.StreamHandler()
    ch.setLevel(level=logging.INFO)
    ch.setFormatter(fm)
    res_logger.addHandler(ch)
    return res_logger


def public_src(src_str1, src_str2):
    if len(src_str1) > len(src_str2):
        src_str1, src_str2 = src_str2, src_str1
    for i in range(len(src_str1), 0, -1):
        for j in range(0, len(src_str1) - i + 1):
            if re.search(src_str1[j: j+i], src_str2):
                return src_str1[j: j+i]


def improve_public(src_str1, src_str2):
    basic_lst = [[0] * len(src_str1) for _ in range(len(src_str2))]
    pub_src = []
    for i in range(len(src_str2)):
        cur_pub = []
        for j in range(len(src_str1)):
            if src_str1[j] == src_str2[i]:
                basic_lst[i][j] = 1
                if i != 0 and j != 0 and basic_lst[i-1][j-1] > 0:
                    basic_lst[i][j] += basic_lst[i-1][j-1]
                if not cur_pub or cur_pub[2] < basic_lst[i][j]:
                    cur_pub = [i, j, basic_lst[i][j]]
        if not cur_pub:
            continue
        if not pub_src:
            pub_src = cur_pub
            continue
        if pub_src[2] < cur_pub[2]:
            pub_src = cur_pub
    if pub_src:
        return src_str1[pub_src[1]-pub_src[2]+1: pub_src[1]+1]


if __name__ == '__main__':
    logger = _logger()
    src1 = ''.join([random.choice(string.digits + string.ascii_lowercase) for _ in range(50)])
    src2 = ''.join([random.choice(string.digits + string.ascii_lowercase) for _ in range(80)])
    logger.info('src1: {}'.format(src1))
    logger.info('src2: {}'.format(src2))
    logger.info('public1: {}'.format(public_src(src1, src2)))
    logger.info('{}'.format('=='*20))
    logger.info('public2: {}'.format(improve_public(src1, src2)))
