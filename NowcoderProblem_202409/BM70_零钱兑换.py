#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 最少货币数
# @param arr int整型一维数组 the array
# @param aim int整型 the target
# @return int整型
#
class Solution:
    ## 如果是用递归的话
    def minMoney(self , arr, aim: int) -> int:
        ## 首先建立一个dp数组，长度为aim+1。
        ## 这个dp数组包含的信息是：当aim为i元的时候，最少需要多少张钞票。
        ## 这个dp数组初始化为无限大。然后再手动定义dp[0]为0，意思是aim为0的时候，需要0张。
        ## 然后每一步去刷新dp的值。在每一步中，去遍历arr里的每一个值。
        dp = [float("inf")] * (aim+1)
        dp[0] = 0
        for i in range(1, aim+1):
            for num in arr:
                if num <= i:
                    dp[i] = min(dp[i], dp[i-num] + 1)
        return dp[-1] if dp[-1] != float("inf") else -1



s = Solution()
print(s.minMoney([5,2, 3], 20))