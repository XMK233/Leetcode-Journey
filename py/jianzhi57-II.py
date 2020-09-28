class Solution:
    def findContinuousSequence(self, target: int):
        if target <= 2: # 最小的target应该是3 -> [1, 2]
            return []
        res = []
        for n in range(2, target+1): # n -> 首尾间隔
            temp = target - n*(n-1)//2
            if temp <= 0:
                break
            if not temp % n: # 首项必为正整数
                start = temp // n
                res.append([start + i for i in range(n)])
        return res[::-1]
# 根据参考的资料, 可知, 利用等差数列求和公式可解此题.
# n就是项数. 这里temp//n得到的就是等差数列的首项, 然后, 这个首项和后面的n-1个数就是要求的一个目标数列.
## 然后遍历所有可能的n值即可. 有的n值会导致temp//n得不到正整数, 那这个n就不行.

# 作者：kosung
# 链接：https://leetcode-cn.com/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof/solution/shu-xue-fa-deng-chai-shu-lie-qiu-he-gong-shi-by-ko/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。