import math
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        ## 暴力求法肯定不行. 得用一点技巧.
        ## 如果是基于Java, 那么最大的int是blabla, 那么不大于blabla的
        ## 最大的3的次方的数就是3^19. 所以, 只要不能整除3^19的数, 就
        ## 肯定不是3的次方.

        # return n > 0 and 1162261467%n==0

        ## 当然, python里面, 整数理论上没有上限. 那事实上上面那个方法
        ## 就失效了. 那就得用一些老方法了.
        ## 比如这个方法我就比较好理解:
        res = math.log(n) / math.log(3)
        print(res, int(res))
        return (res - int(res) == 0)

s = Solution()
print(s.isPowerOfThree(1162261467))
