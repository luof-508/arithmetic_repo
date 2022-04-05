"""
排序算法
"""


class Bubble:
    """
    冒泡法
    冒泡法是一种交换排序，
    升序：n个数从左到右，编号从0到n-1，索引0和1的值比较，如果索引0大，则交换二者位置，如果索引1大，则不必交互；继续比较索引1和索引2的值...
    将最大值放到右侧；继续找次大值，周而复始，直至剩下最后两个数比较
    复杂度：遍历次数1...n-1和为(n-1)*(n-2)/2,时间复杂度O（n^2）
    """
    @staticmethod
    def bubble_sort(lst):
        n, con_swap, con = len(lst), 0, 0
        for i in range(n-1):
            for j in range(n-1):
                con += 1
                if lst[j] < lst[j+1]:
                    con_swap += 1
                    lst[j], lst[j+1] = lst[j+1], lst[j]
        return lst, con_swap, con

    @staticmethod
    def bubble_sort_improve(lst):
        n, con_swap, con = len(lst), 0, 0
        for i in range(n-1):
            flag = False
            for j in range(n-1):
                con += 1
                if lst[j] < lst[j+1]:
                    flag = True
                    con_swap += 1
                    lst[j], lst[j+1] = lst[j+1], lst[j]
            if not flag:
                break
        return lst, con_swap, con

    @staticmethod
    def bubble_rep(src):
        n = len(src)
        print(src)
        for i in range(n-1):
            exc = False
            for j in range(0, n-1-i):
                if src[j] > src[j+1]:
                    exc = True
                    src[j], src[j+1] = src[j+1], src[j]
            if not exc:
                break
        print(src)


class SortArithmetic:
    """
    # 选择排序:不稳定算法
    # 遍历列表，找到当前循环的极值索引index，然后将这个极值与指定的有序区一端元素位置交换
    # 选择排序的优点：交换少，每次遍历只需交换一次，但是剩下的无序区无法判断是否有序。
    # 长度为n的序列，遍历次数 n*(n-1)/2。复杂度为：O(n^2)
    """
    @staticmethod
    def select_sort(lst):
        n, con_swap, con = len(lst), 0, 0
        for i in range(n):
            max_index = i
            for j in range(i+1, n):
                con += 1
                if lst[max_index] < lst[j]:
                    max_index = j
            if max_index != i:
                lst[i], lst[max_index] = lst[max_index], lst[i]
                con_swap += 1
        return lst, con_swap, con

    @staticmethod
    def select_sort_binary_opr(lst):
        print(lst)
        n, con_swap, con = len(lst), 0, 0
        for i in range(n//2):
            max_idx = i
            min_idx = -1-i
            origin_min_idx = min_idx
            for j in range(i+1, n):
                con += 1
                if lst[max_idx] < lst[j]:
                    max_idx = j
                if lst[min_idx] > lst[-1-j]:
                    min_idx = -1-j
            if min_idx == max_idx:
                break
            if max_idx != i:
                lst[max_idx], lst[i] = lst[i], lst[max_idx]
                con_swap += 1
                if min_idx == i or min_idx == i - n:
                    min_idx = max_idx
            if min_idx != origin_min_idx:
                lst[min_idx], lst[origin_min_idx] = lst[origin_min_idx], lst[min_idx]
                con_swap += 1
        print(lst)
        return lst, con_swap, con

    @staticmethod
    def select_rep(src):
        """
        遍历元素,找出无序区最大值，记录索引，最后交换
        :param src:
        :return:
        """
        n = len(src)
        print(src)
        for i in range(n//2):
            max_idx = i
            min_idx = n-1-i
            for j in range(i+1, n):
                if src[max_idx] < src[j]:
                    max_idx = j
                if src[min_idx] > src[n-1-j]:
                    min_idx = n-1-j
            if max_idx == min_idx:
                break
            if max_idx != i:
                src[i], src[max_idx] = src[max_idx], src[i]
                if min_idx == i:
                    min_idx = max_idx
            if min_idx != n-1-i:
                src[min_idx], src[n-1-i] = src[n-1-i], src[min_idx]
        print(src)


class InsertArithmetic:
    @staticmethod
    def insert_sort(src):
        return


if __name__ == '__main__':
    lst1 = [[1, 9, 8, 5, 6, 7, 4, 3, 2],
            [1, 1, 1, 1, 1, 1, 1, 1, 1]]
    # sort_lst, con_swaps, cons = SortArithmetic.select_sort(lst1)
    # print(sort_lst, con_swaps, cons)
    # lst1 = [1, 9, 8, 5, 6, 7, 4, 3, 2]
    # sort_lst, con_swaps, cons = SortArithmetic.select_sort_binary_opr(lst1)
    # print(sort_lst, con_swaps, cons)
    # sort_lst, con_swaps, cons = Bubble.bubble_sort(lst1[0])
    # print(sort_lst, con_swaps, cons)
    # lst1 = [[1, 9, 8, 5, 6, 7, 4, 3, 2],
    #         [1, 1, 1, 1, 1, 1, 1, 1, 1]]
    # sort_lst, con_swaps, cons = Bubble.bubble_sort_improve(lst1[0])
    # print(sort_lst, con_swaps, cons)
    SortArithmetic.select_rep(lst1[0])

