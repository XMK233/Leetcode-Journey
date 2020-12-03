class Solution:
    def add(self, a: int, b: int) -> int:
        # 32位数掩码
        mask = 0XFFFFFFFF
        # 32位数的最大正数
        posMx = 0X7FFFFFFF
        while b != 0:
            # a是不带进位的和, 都要转成32位整数
            # b是进位, 都要转成32位整数
            # 循环直到进位为0, 那么a就是最终结果
            smwithoutcarry = (a ^ b) & mask
            carry = ((a & b) << 1) & mask
            a, b = smwithoutcarry, carry
        # 最终如果是32位负数的话, 需要将其转回python正常的负数表示形式(高于32位的全是1, 而不是32位负数那样更高位全为0), 做法是先对低 32 位的取反, 更高位不变, 然后整体再取反, 从而将大于等于 32 位的数字重新转成 1
        return a if a <= posMx else ~(a ^ mask)

### https://blog.csdn.net/zjulyx1993/article/details/108245454