import string


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# class Solution:
#     def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
#         node1, node2 = headA, headB
#         while node1 != node2:
#             node1 = node1.next if node1 else headB
#             node2 = node2.next if node2 else headA
#         return node1
class Solution:

    @staticmethod
    def max_frequency(nums: list, k: int) -> int:
        """
        [[0, 1, 25], [2, 3, 123], [0, 3, 55], [2, 3, 76]]
        :param nums:
        :param k:
        :return:
        """
        n = len(nums)
        seq = sorted(nums, key=lambda x: x[0])
        teams = set()
        values = set()
        j = 0
        max_value = float('inf')
        while seq[j][0] == 0:
            flag = 1
            teams.add(seq[j][0])
            teams.add(seq[j][1])
            values.add(seq[j][2])
            for cur_team in seq[j:]:
                if cur_team[0] == 0:
                    continue
                if cur_team[0] not in teams and cur_team[1] not in teams:
                    flag += 1
                    teams.add(cur_team[0])
                    teams.add(cur_team[1])
                    values.add(cur_team[2])
                if flag == k:
                    break
            if flag == k:
                max_value = min(max(values), max_value)
            # 下一次循环前将teams, values清空
            teams.clear()
            values.clear()
            # i遍历到列表最后一个元素
            j += 1
            if j >= n:
                break

        return max_value

    @staticmethod
    def maximumTime(time: str) -> str:
        # 23：59 00：00
        # 第一位0--2
        # 第二位0-1：0-9， 2：0-3
        # 第三位0-5
        # 第四位0-9
        one = time[0]
        two = time[1]
        three = time[3]
        four = time[4]
        print(three)
        a = ''
        b = ''
        if one == '?' and two != '?':
            a = '2' + two
        elif one == '?' and two == '?':
            a = '23'
        elif one in ['0', '1'] and two == '?':
            a = one + '9'
        elif one in ['2'] and two == '?':
            a = one + '3'
        else:
            a = one + two

        if three == '?' and four != '?':
            b = '5' + four
        elif three == '?' and four == '?':
            b = '59'
        elif three != '?' and four == '?':
            b = three + '9'
        else:
            b = three + four
        return a + ':' + b

    @staticmethod
    def is_covered(ranges: list, left: int, right: int) -> bool:
        for i in range(left, right+1):
            flag = False
            for ra in ranges:
                if ra[0] <= i <= ra[1]:
                    flag = True
                    break
            if not flag:
                return False
        return True


if __name__ == '__main__':
    inputs2 = 2
    inputs1 = [[0, 1, 25], [2, 3, 123], [0, 3, 55], [1, 3, 76]]
    # inputs1 = [[0, 1, 23]]
    # inputs2 = 1
    # res2 = Solution.max_frequency(inputs1, inputs2)
    # print(res2)
    ranges = [[1, 4], [0, 9]]
    print(Solution.is_covered(ranges, 2, 6))


