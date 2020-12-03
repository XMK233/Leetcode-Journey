# https://leetcode-cn.com/problems/yuan-quan-zhong-zui-hou-sheng-xia-de-shu-zi-lcof/solution/javajie-jue-yue-se-fu-huan-wen-ti-gao-su-ni-wei-sh/
class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        l = [i for i in range(n)]
        idx = 0
        while n > 1:
            idx = (idx + m - 1)%n
            del l[idx]
            n -= 1
        return l[0]

## 这种方法比较好理解, 也就是说每一次都删掉(idx + m - 1)模上n的值.
## 为什么要模上n呢? 因为是循环的嘛.