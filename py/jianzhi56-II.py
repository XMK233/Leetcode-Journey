class Solution:
    def singleNumber(self, nums) -> int:
        res = 0
        for i in range(32):
            cnt = 0  # 记录当前 bit 有多少个1
            bit = 1 << i  # 记录当前要操作的 bit
            for num in nums:
                if num & bit != 0:
                    cnt += 1
            if cnt % 3 != 0:
                # 不等于0说明唯一出现的数字在这个 bit 上是1
                res |= bit

        return res - 2 ** 32 if res > 2 ** 31 - 1 else res


## https://www.pythonheidong.com/blog/article/251304/
## https://leetcode-cn.com/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-ii-lcof/solution/mian-shi-ti-56-ii-shu-zu-zhong-shu-zi-chu-xian-d-4/
## 解释地很清楚. 思路可以说是非常明显了. 关键就是求解了.
## 第二个链接给的求解方法比较高端, 第一个链接给的方法就比较直白, 但是肯定不是最好的.