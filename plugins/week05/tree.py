# coding = utf-8
"""
二叉树的性质：
性质1、在二叉树第i层，至多有2^(i-1)个节点
性质2、深度为n的二叉树，最多有2^(n)-1个节点
性质3、对应任何一课二叉树，如果其终端节点数为n0，度数为2的节点数为n2，则有n0=n2+1
性质4、含有n个节点的完全二叉树，深度为：int(log2(n))+1或math.ceil(log2(n+1))
性质5、一棵n个节点的完全二叉树：假设根节点序号i=1，则其第m个节点有：
      当2*m <= n,则节点m有左孩子；
      当2*m + 1 <= n,则节点m有右孩子。
其他性质、含有n个节点的二叉树，高度至多为n、至少为math.ceil(log2(n+1))

树的遍历：对树中所有元素不重复的遍历一遍
广度优先：层序遍历
深度优先：前序遍历、中序遍历、后序遍历
遍历序列：将树中所有元素遍历后，得到的元素序列。将层次结构转换为线性结构

二叉树的遍历：左子树必须在右子树的前面。深度优先中的前、中、后是指根节点位于遍历序列中的前面、中间或后面   递归遍历


堆排序：
堆是一个完全二叉树
大顶堆：每一个非叶子节点都要大于等于左右孩子。小顶堆则相反
根节点：一定是大顶堆中的最大值，小顶堆打最小值
稳定：序列中，值相同的不同元素，顺序也是稳定的
排序过程：1、首先写一个函数，实现对单个叶子进行调整 -- 首次调整为大顶堆；拿走极值后，对跟节点进行堆调整
"""
__author__ = 'fg.luo'

import logging
import math
import random
import time


def set_log():
    # 实例化日志
    _logger = logging.getLogger(__name__)
    _logger.setLevel(level=logging.INFO)  # logger等级总开关
    # 创建一个控制台handler
    ch = logging.StreamHandler()
    # 定义handler输出格式
    formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
    ch.setFormatter(formatter)
    ch.setLevel(level=logging.INFO)
    _logger.addHandler(ch)
    return _logger


logger = set_log()


class HeapSolution:
    def __init__(self, seq: list):
        self.seq = [0] + seq
        self.num = len(seq)
        self.depth = math.ceil(math.log2(self.num + 1))

    def heap_sort_procedure(self):
        logger.info('Start to change the origin seq as a big heap')
        self.big_heap()

        logger.info('Swap the root node with the last leaf node, and re sort the rest of seq as a big heap')
        for i in range(self.num, 0, -1):
            self.seq[1], self.seq[i] = self.seq[i], self.seq[1]
            logger.info('re sort as a big heap')
            self.loop_point(1, 1, i-1)
            logger.info('re sort result:{}'.format(self.seq[1:i-1]))

        logger.info('sort result: {}'.format(self.seq[1:]))
        return self.seq[1:]

    def big_heap(self):
        """
        构造大顶堆
        :return:
        """
        logger.info('Origin seq:{}'.format(self.seq[1:]))
        logger.info('Sort the tree as a big heap')
        start_point = self.num // 2
        cur_layer = math.ceil(math.log2(start_point+1))
        logger.info('depth of the tree:{}'.format(self.depth))
        for i in range(start_point, 0, -1):
            if i <= 2*(cur_layer-1) - 1:
                cur_layer -= 1
            self.loop_point(i, cur_layer, self.num)
        logger.info('big heap result:{}'.format(self.seq[1:]))
        time.sleep(1)
        logger.info('print big heap>>>>>')
        self.print_tree(self.seq[1:])

    def loop_point(self, point, layer, seq_len):
        """
        实现对堆进行调整
        :param point:
        :param layer:
        :param seq_len:
        :return:
        """
        self._heap_method(point, seq_len)
        left_idx, right_idx = 2*point, 2*point + 1
        if left_idx <= seq_len:
            self.loop_point(left_idx, layer + 1, seq_len)
        if right_idx <= seq_len:
            self.loop_point(right_idx, layer + 1, seq_len)

    def _heap_method(self, point, seq_len):
        """
        实现对叶子节点进行调整
        :param point:
        :return:
        """
        if 2*point <= seq_len < 2*point + 1:
            _left = 2*point
            if self.seq[point] < self.seq[_left]:
                self.seq[point], self.seq[_left] = self.seq[_left], self.seq[point]
        elif 2*point + 1 <= seq_len:
            max_son_idx = 2*point if self.seq[2*point] > self.seq[2*point+1] else 2*point+1
            if self.seq[point] < self.seq[max_son_idx]:
                self.seq[point], self.seq[max_son_idx] = self.seq[max_son_idx], self.seq[point]

    @staticmethod
    def print_tree(seq):
        """
        打印一棵树
        间距规律：高度为n的完全二叉树，节点间的间距为8个字符(包含上一层双亲数字占位),单个数字占位为2个字符串,
                   则 第x层第一个数字的缩进为 节点间的间距 + 字符占位：(2**(n-x) - 1) * 3 + 2**(n-x-1) * 2
                每一层计算方法： 缩进 + 字符占位 + 字符间距
        :param seq:
        :return:
        """
        layer = math.ceil(math.log2(len(seq)+1))
        last_sep = '        '  # 最后一层节点间距8个字符串
        str_sep = len(str(max(seq))) * ' '  # 单个数字占位
        half_sep = '   '  # 半个间距3个字符
        str_lst = []
        logger.info('layer:{}, the seq:{}'.format(layer, seq))
        for i in range(layer, 0, -1):
            all_front_layer = 2**(i-1) - 1
            start_idx = all_front_layer
            cur_num = 2**(i-1)
            cur_print = ''
            if i < layer:
                tuck = (2**(layer-i) - 1) * half_sep + 2**((layer-i)-1) * str_sep
                cur_print = tuck + cur_print
            for _ in range(cur_num):
                cur_print = cur_print + '{:^2}'.format(seq[start_idx]) + 2**(layer-i) * last_sep + (2**(layer-i)-1) * str_sep
                start_idx += 1
                if start_idx == len(seq):
                    break
            str_lst.append(cur_print)
        for s in range(len(str_lst)-1, -1, -1):
            print(str_lst[s])


if __name__ == '__main__':
    origin = [random.choice(range(1000)) for s in range(int(input('enter the length>>>')))]
    heap_sol = HeapSolution(origin)
    heap_sol.print_tree(origin)
    res = heap_sol.heap_sort_procedure()
