class FactorialRecursion:
    """
    求n的阶乘
    n! = n * (n-1) * ... * 1 = n * (n-1)!
    """
    @staticmethod
    def factorial_func(n, fac=1):
        for i in range(1, n + 1):
            fac *= i
        return fac

    def factorial_by_recursion(self, n):
        """
        使用递归
        :param n:
        :return:
        """
        if n == 1:
            return 1
        return self.factorial_by_recursion(n-1) * n


class ReverseNum:
    """
    将一个数字倒序输出为列表
    """
    @staticmethod
    def reverse_num(num):
        res = list()
        for num_str in str(num):
            res.insert(0, int(num_str))
        return res

    def reverse_num_by_recursion(self, num, res=None):
        str_num = str(num)
        if not res:
            res = list()
        if not str_num:
            return res
        res.append(int(str_num[-1]))
        return self.reverse_num_by_recursion(str_num[:-1], res)


class MonkeyPeach:
    @staticmethod
    def total_peach(day=10):
        """
        一天吃掉一半桃子 + 1
        第10天只剩1个: n-1 = [num(n) + 1] * 2
        :param day:
        :return:
        """
        rest = 1
        for i in range(day-1, 0, -1):
            rest = (rest + 1) * 2
        return rest

    def total_peach_by_recursion(self, day=10, rest=1):
        if day == 1:
            return rest
        rest = (rest + 1) * 2
        return self.total_peach_by_recursion(day-1, rest)


if __name__ == "__main__":
    # print(FactorialRecursion.factorial_func(100))
    # print('----------------')
    # print(FactorialRecursion().factorial_by_recursion(998))
    print(ReverseNum.reverse_num(1))
    print(ReverseNum().reverse_num_by_recursion(1234))
    # print(MonkeyPeach.total_peach())
    # print(MonkeyPeach().total_peach_by_recursion())
