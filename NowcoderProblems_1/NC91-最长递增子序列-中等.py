# -*- coding:utf-8 -*-
'''
https://www.nowcoder.com/practice/9cf027bf54714ad889d4f30ff0ae5481?tpId=117&&tqId=37796&&companyId=665&rp=1&ru=/company/home/code/665&qru=/ta/job-code-high/question-ranking

题目描述
给定数组arr，设长度为n，输出arr的最长递增子序列。（如果有多个答案，请输出其中字典序最小的）
示例1
输入
复制
[2,1,5,3,6,4,8,9,7]
返回值
复制
[1,3,4,8,9]
示例2
输入
复制
[1,2,8,6,4]
返回值
复制
[1,2,4]
说明
其最长递增子序列有3个，（1，2，8）、（1，2，6）、（1，2，4）其中第三个字典序最小，故答案为（1，2，4）
备注:
n \leq 10^5n≤10
5

1 \leq arr_i \leq 10^91≤arr
i
​
 ≤10
9

参考的思路：
我们用dp[i]表示数组的前i个元素构成的最长上升子序列，
如果要求dp[i]，我们需要用num[i]和前面的数字一个个比较，如果比前面的任何一个数字大，说明加入到他的后面可以构成一个上升子序列 ，就更新dp[i]。

上述思路只能求最长的递增序列是多长，不能得到最长序列本身。tnd。

'''
class Solution:
    def LIS(self , arr ):
        pass
    def longestIncreasingOrder(self, arr):
        # write code here
        dp = [1 for _ in range(len(arr))]
        for i in range(1, len(arr)):
            ## print("-------------{}_________".format(arr[i]))
            # for j in range(0, i):
            for j in range(i - 1, -1, -1):
                ## print(dp[j])
                if arr[i] > arr[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        print(dp)
        return dp[-1]

s = Solution()
print(s.LIS([8, 2, 3, 1, 4]))
