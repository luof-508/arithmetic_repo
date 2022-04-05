# !/usr/bin/python
# coding: utf-8


class JulyExerciseList(object):
    def __init__(self):
        pass

    @staticmethod
    def frequency_sort(src: str) -> str:
        """
        给定一个字符串，请将字符串里的字符按照出现的频率降序排列

        :param src: "tree"
        :return: "eert"
        """
        record_dic = dict()
        for s in src:
            if not record_dic.get(s):
                record_dic[s] = 1
                continue
            record_dic[s] += 1
        res_sort = sorted(record_dic.items(), key=lambda x: x[1], reverse=True)
        result = ''
        for s, num in res_sort:
            result += s*num
        return result

    @staticmethod
    def seq_sort(src: str) -> str:
        """
        给定一个字符串，请将字符串里的字符按照出现的频率降序排列

        :param src: 'tree'
        :return: 'eetr'
        """
        str_record = list()
        num_list = list()
        for s in src:
            if s not in str_record:
                str_record.append(s)
                num_list.append(1)
                continue
            i = str_record.index(s)
            num_list[i] = num_list[i] + 1
        for i in range(1, len(num_list)):
            for j in range(0, i):
                if num_list[i] > num_list[j]:
                    num_list[i], num_list[j] = num_list[j], num_list[i]
                    str_record[i], str_record[j] = str_record[j], str_record[i]
        res = ''
        for i, s in enumerate(str_record):
            res = res + num_list[i] * s
        return res

    @staticmethod
    def find_error_num(src):
        """
        集合 src 包含从 1 到n的整数。不幸的是，因为数据错误，导致集合里面某一个数字复制了成了集合里面的另外一个数字的值，
        导致集合 丢失了一个数字 并且 有一个数字重复 。
        给定一个数组 nums 代表了集合 src 发生错误后的结果。请你找出重复出现的整数，再找到丢失的整数，将它们以数组的形式返回。

        :param src:
        :return:
        """
        seq_list = sorted(src)
        n = len(seq_list)
        rep = None
        for i in range(1, n):
            if seq_list[i] == seq_list[i-1]:
                rep = seq_list[i]
                break
        right = set(range(1, n+1))
        lost = right.difference(set(src)).pop()
        return [rep, lost]

    @staticmethod
    def count_atom(formula: str) -> str:
        """
        考察压栈出栈
        formula = "K4(ON(SO3)2)2"

        :param formula:
        :return:
        """
        n = len(formula)
        i = 0
        flag = 0
        stack = []
        while i < n:
            # 查找单个原子表达式和数量，以及栈的初始值
            atom = ['', 1, flag]
            if formula[i].isupper():
                atom[0] = atom[0] + formula[i]
                i += 1
                while i < n and formula[i].islower():
                    atom[0] += formula[i]
                    i += 1
                if i < n and formula[i].isdigit():
                    atom[1] = int(formula[i])
                    i += 1
                stack.append(atom)

            # 遇到左括号，加一层栈
            elif formula[i] == '(':
                flag += 1
                i += 1
            # 遇到右扩号，查找将对应一层栈原子需要乘的数字，并在存的栈列表里，查找对应一层栈的原子，乘以倍数后，栈降低一层
            elif formula[i] == ')':
                i += 1
                multi = 1
                if formula[i].isdigit():
                    multi = int(formula[i])
                    i += 1
                end = len(stack)
                while stack and stack[end-1][2] == flag:
                    stack[end-1][1] = stack[end-1][1] * multi
                    stack[end-1][2] = stack[end-1][2] - 1
                    end -= 1
                flag -= 1

        # 处理合并栈内相同的元素
        stack_dic = dict()
        for tmp_atom in stack:
            stack_dic[tmp_atom[0]] = stack_dic.get(tmp_atom[0], 0) + tmp_atom[1]

        # 按字典序输出
        res = sorted(stack_dic.items(), key=lambda x: x[0])
        result = ''
        for atom, num in res:
            multi = '' if num == 1 else str(num)
            result += atom + multi

        return result

    def count_pairs(self, deliciousness: list) -> int:
        """
        计算两种餐品和为2的幂

        :param deliciousness:
        :return:
        """
        num = 0
        n = len(deliciousness)
        exist = set()
        for i in range(n-1):
            first_num = deliciousness[i]
            for j in range(i+1, n):
                second_num = deliciousness[j]
                sum_res = first_num + second_num
                if sum_res == 2 or sum_res == 1:
                    num += 1
                    exist.add(sum_res)
                    continue
                elif sum_res in exist:
                    num += 1
                    continue
                else:
                    boolean_value, exist_set = self.back_method(sum_res)
                    if boolean_value:
                        num += 1
                        exist.update(exist_set)
        return num

    def back_method(self, src, exist=None):
        if not exist:
            exist = set()
        exist.add(src)
        if src == 1:
            return True, exist
        elif src % 2:
            return False, set()
        tmp = src // 2
        exist.add(tmp)
        return self.back_method(tmp, exist)

    @staticmethod
    def num_sub_array_with_sum(nums: list, goal: int) -> int:
        """
        给定一个二元数组nums， 和一个数goal
        计算有多少子数组sub，其元素和等于goal
        
        :param nums: 
        :param goal: 
        :return: 
        """
        # nums[i]不是0就是1
        # 1 <= nums.length <= 3 * 10**4
        # 0 <= goal <= nums.length

        # 从 length == goal开始取子集
        # 当遍历同一长度的子集后，都大于goal时，停止
        result = 0
        n = 1
        start_len = 1
        while n <= len(nums):
            flag = 0
            for i in range(0, len(nums) + 1 - start_len):
                sub = nums[i: i+start_len]
                if sum(sub) == goal:
                    result += 1
                else:
                    flag += 1
            if flag == len(nums) + 1 - start_len and result > 0:
                break
            start_len += 1
            n += 1

        return result

    # @staticmethod
    # def numSubarraysWithSum(nums: list[int], goal: int) -> int:
    #     from collections import Counter
    #     res = 0
    #     sum1 = 0
    #     c = Counter()
    #     for num in nums:
    #         c[sum1] += 1
    #         sum1 += num
    #         res += c[sum1-goal]
    #     return res


class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # 总计调用120000.提前开辟空间？
        self.dic = dict()
        self.key = [''] * 120001
        self.value = [''] * 120001
        self.timestamp = [0] * 120001

    def set(self, key: str, value: str, timestamp: int) -> None:
        """
        1、每次存储时，如果key/value存在，则更新时间戳

        :param key:
        :param value:
        :param timestamp:
        :return:
        """
        # key = 'food' value1 = 'hi1' stamp = 32
        # 总计调用120000次，时间搓递增。时间搓作为索引下标，并将时间搓填入对应的位置
        self.timestamp[timestamp] = timestamp
        self.key[timestamp] = key
        self.value[timestamp] = value



        # if not self.dic.get(key):
        #     self.dic[key] = {'value': [value], 'timestamp': [timestamp]}
        # else:
        #     self.dic[key].get('value').append(value)
        #     self.dic[key].get('timestamp').append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        """
        1、如果get到key value，对比时间戳，当存储的时间戳大于输入，返回''
        2、1 <= timestamp <= 10**7

        :param key:
        :param timestamp:
        :return:
        """
        if self.timestamp[timestamp] == 0:
            for i in range(timestamp-1, 0, -1):
                if self.timestamp[i] > 0 and self.key[i] == key:
                    return self.value[i]
        else:
            if self.key[timestamp] == key:
                return self.value[timestamp]
        return ''





        # res = self.dic.get(key)
        # if not res:
        #     return ''
        # time_lst = res.get('timestamp')
        # if timestamp in time_lst:
        #     tmp_index = time_lst.index(timestamp)
        #     return res.get('value')[tmp_index]
        # elif timestamp < time_lst[0]:
        #     return ''
        # else:
        #     for i in range(len(time_lst)-1, -1, -1):
        #         if time_lst[i] < timestamp:
        #             return res.get('value')[i]

    @staticmethod
    def mains(put1, put2):
        lst = []
        for i, style in enumerate(put1):
            if style == 'set':
                key, value, timestamp = put2[i]
                obj.set(key, value, timestamp)
                lst.append(None)
            else:
                key, timestamp = put2[i]
                param_2 = obj.get(key, timestamp)
                lst.append(param_2)
        return lst


class MajorityElement(object):
    def __init__(self):
        pass

    @staticmethod
    def majority_element(nums: list) -> int:
        """

        :param nums:
        :return:
        """
        n = len(nums)
        record_dict = dict()
        for s in nums:
            if not record_dict.get(s):
                record_dict[s] = 1
                continue
            record_dict[s] += 1
        res = sorted(record_dict.items(), key=lambda x: x[1])
        if res[-1][1] * 2 > n:
            return res[-1][0]
        return -1

    @staticmethod
    def majority_element_improve(nums: list) -> int:
        """

        :param nums:
        :return:
        """
        from collections import Counter
        count_list = sorted(Counter(nums).items(), key=lambda x: x[1])
        if count_list[-1][1] * 2 > len(nums):
            return count_list[-1][0]
        return -1

    @staticmethod
    def majority_element_improve_prove(nums: list) -> int:
        """
        投票算法。消消乐

        :param nums:
        :return:
        """
        n = len(nums)
        cur = -1
        record_people = 0
        for num in nums:
            if not record_people:
                cur = num
            if cur == num:
                record_people += 1
            else:
                record_people -= 1

        return cur if record_people and nums.count(cur) * 2 > n else -1


class HIndex(object):

    @staticmethod
    def high_index(citations: list) -> int:
        """

        :param citations:
        :return:
        """
        from collections import Counter
        citation_statistic = sorted(Counter(citations).items(), key=lambda x: x[0])
        h_list = list()
        for i, item in enumerate(citation_statistic):
            # 被引用次数 > 对应的论文数
            be_cited_times, paper_nums = item
            # [1, 11]
            if be_cited_times <= paper_nums:
                h_list.append(be_cited_times)
            # [11, 2], [12, 3], [13, 14]
            else:
                sums = 0
                for _, num in citation_statistic[i:]:
                    sums += num
                    if sums >= be_cited_times:
                        break
                if sums >= be_cited_times:
                    h_list.append(be_cited_times)
                else:
                    h_list.append(sums)
        return sorted(h_list)[-1]

    @staticmethod
    def improve(citations: list) -> int:
        from collections import defaultdict
        citations = sorted(citations)
        counter = defaultdict(int)
        n = len(citations)
        print(citations)
        for i in range(n):
            # 排序后，从[i,n]的文章引用次数都是大于citations[i]的，所以直接计数候选h指数为n-1
            counter[citations[i]] = n - i
            print(counter)
            # 即题意中“h 指数是指他（她）的 （N 篇论文中）总共有 h 篇论文分别被引用了至少 h 次”
            if n - i <= citations[i]:
                return n - i

        return 0


class MinAbsoluteSumDiff(object):

    @staticmethod
    def min_absolute_sum_diff(nums1: list, nums2: list) -> int:
        """

        :param nums1:
        :param nums2:
        :return:
        """
        import bisect
        # 1 求两个列表的差值绝对值和，若果和为0，直接返回
        n = len(nums1)
        diff = sum([abs(nums1[i] - nums2[i]) for i in range(n)])
        if not diff:
            return 0
        ans = float('Inf')
        # 2 对nums1进行升序排序
        nums_seq = sorted(nums1)
        # 3 使用bisect模块，遍历循环nums2的元素，通过插值法查找nums2每一个元素nums2[j]，对应排序后nums1中与nums2[j]最接近的元素索引。
        # 4 比较替换索引附近两个元素，取差值最小的作为替换元素
        for j, num_j in enumerate(nums2):
            # bisect_left返回nums1中与num_j最接近的x索引，若果有多个x，返回最左边的一个x对应的索引
            idx = bisect.bisect_left(nums_seq, num_j)
            if idx:
                # [1 -> num_seq[idx-1], 3 -> num_seq[idx]]
                ans = min(ans, diff - abs(nums1[j] - nums2[j]) + abs(nums_seq[idx-1] - num_j))
            if idx < n:
                ans = min(ans, diff - abs(nums1[j] - nums2[j]) + abs(nums_seq[idx] - num_j))
        return ans % (10 ** 9 + 7)


class MaximumElementAfterDecrementingAndRearranging(object):
    @staticmethod
    def maximum_element_after_decrementing_and_rearranging(arr: list) -> int:
        """
        贪心算法
        1、升序排列
        2、第一个数定义为1
        3、当后一个数减前一个数大于1，则后一个数等于前一个数+1，因为最多+1（提目限制只能加不能减）

        :param arr:
        :return:
        """
        n = len(arr)
        arr_seq = sorted(arr)
        arr_seq[0] = 1
        for i in range(1, n):
            if arr_seq[i] - arr_seq[i-1] > 1:
                arr_seq[i] = arr_seq[i-1] + 1
        print(arr_seq)
        return arr_seq[-1]


class MaxArray(object):
    @staticmethod
    def max_array(nums):
        """
        暴力解
        求序列的最大子序列和
        :param nums: [-2,1,-3,4,-1,2,1,-5,4],
        :return:
        """
        if not nums:
            return

        n = len(nums)
        if not n:
            return
        ans = float('-inf')
        for i in range(1, n+1):
            for j in range(0, n-i+1):
                # i=2 j=0
                sub_array = sum(nums[j: j + i])
                ans = max(ans, sub_array)
        return ans

    @staticmethod
    def max_array_improve(nums: list) -> int:
        """
        动态规划
        求序列的最大子序列和

        1、包含nums[i]在内的前i项最大子序和为D[i]
        a、当第i项≤0时，D[i] = D[i-1]
        b、当第i项＞0时，D[i] = max(D[i-1]+arr[i], D[i-1])
        :param nums:
        :return:
        """
        # 前i项元素的包含nums[i]在内打最大子序和为dp[i]
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        ans = dp[0]
        for i in range(1, n):
            # 前i项元素，包含nums[i]在内的最大子序和
            dp[i] = max(dp[i-1] + nums[i], nums[i])
            print(dp[i], nums[i])
            # ans记录了前i项的最大自序和
            ans = max(dp[i], ans)
        return ans

    @staticmethod
    def maxSubArray(nums: list) -> int:
        l = len(nums)
        # 特殊情况判断
        if l<1:
            return 0
        elif l==1:
            return nums[0]

        # 初始化赋值
        D = [0] * l
        D[-1] = nums[-1]
        max = D[-1]

        i = l-2  # 注意，i是从l-2开始，也就是倒数第二位开始，因为倒数第一位已经初始化赋值nums[-1]了
        while i>=0:
            if D[i+1]>0:
                D[i] = nums[i] + D[i+1]
            else:
                D[i] = nums[i]
            if D[i]>max:
                max = D[i]
            i = i-1
            print(max)
        return max


class GroupGrams:

    @staticmethod
    def group_grams(strings: list) -> list:
        import collections
        default_dict = collections.defaultdict(list)
        for strs in strings:
            seq_str_lst = ''.join(sorted(strs))
            default_dict[seq_str_lst].append(strs)
        return list(default_dict.values())


if __name__ == '__main__':
    obj = MinAbsoluteSumDiff()
    inputs1 = [1, 7, 5]
    inputs2 = [2, 3, 5]
    result = obj.min_absolute_sum_diff(inputs1, inputs2)
    print(result)

