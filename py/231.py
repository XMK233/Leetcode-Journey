class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        ## 大佬的思路：n和n-1按位与，得0，则为幂。
        ## 要注意，边界条件如果是0，1之类，属于特殊情况，需要另行对待。
        if n == 0:
            return False
        if n == 1:
            return True
        return (n & (n - 1) == 0)
        ## 我的思路：反正就是1打头后面皆是0的数字就对了。
        ## 那就酱紫：这个数右移一位，再左移一位，如果跟原来有出入，就包含不止一个1，那就肯定不是2的幂
        ## 这个会超时
        # n1 = n
        # while n1 != 1:
        #     tmp = n1>>1<<1
        #     if tmp != n1:
        #         return False
        #     n1 = n1 >> 1
        # return True

s = Solution()
print(s.isPowerOfTwo(4))