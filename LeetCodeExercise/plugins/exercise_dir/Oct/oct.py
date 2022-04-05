class IntToHex:
    """
    十六进制：0-9abcdef
    负数用补码：
    原码：最高位是符号位；5 -> 0b101
    反码：正数的反码与原码相同；负数的反码符号位不变，其余按位取反，
    补码：正数的补码与原码相同，负数的补码符号位不变，其余按位取反后+1
         补码的补码是原码

    -1: 'f0000001' -> 补码：‘ffffffff’
    -32:'f0000020' -> 补码：‘ffffff0e’
    加法：最高位溢出舍弃
    32 20
    """
    @staticmethod
    def int_to_hex(num: int) -> str:
        hex_digit = dict(zip(range(16), '0123456789abcdef'))
        res = []
        _num = num
        for _ in range(8):
            cur = _num // 16
            tmp = _num % 16
            res.append(hex_digit.get(tmp))
            if cur == 0:
                break
            _num = cur
        res.reverse()
        return ''.join(res)


class Solution:
    def toHex(self, num: int) -> str:
        CONV = "0123456789abcdef"
        ans = []
        # 32位2进制数，转换成16进制 -> 4个一组，一共八组
        for _ in range(8):
            # 当输入值num为-1 ，第一次进入循环
            ans.append(num % 16)  # num % 16 = 15
            num //= 16  # num // 16 = -1
            # Python中的//运算取整除：向下取接近商的整数
            # %取模运算返回整除的余数 （余数 = 被除数 - 除数 * 商）
            # 负整数 // 正整数 的最大值为-1
            #   -1 // 16 = -1
            #   -1 % 16 = 15
            #   即如num为负数，则一定会跑满for的8次循环
            # 正整数 // 正整数 的最小值为0
            #   1 // 16 = 0
            #   1 % 16 = 1
            #   即num为正数时，有可能触发下面的if语句，提前结束for循环
            if not num:  # 如果num不为0则继续下一次for循环
                break  # 如果num为0则终止for循环
            # 正整数 // 负整数 的最大值为-1，如1 // -16 = -1; 1 % -16 = -15
        return "".join(CONV[n] for n in ans[::-1])

if __name__ == '__main__':
    num = -1
    # print(IntToHex.int_to_hex(num))
    # print(-2//16)
    lst = 'abcdef'
    print(lst[0:-1:2])
