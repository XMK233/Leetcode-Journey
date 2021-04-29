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
import bisect
class Solution:
    def LIS(self , arr ):
        # write code here
        n = len(arr)
        dp = [1] * n
        lenth = 1
        array = [arr[0]] ## 四舍五入, array是用来记录最长子序列本身的. 并不是说array就是真的记录最长子序列本身的, 只能说大概是.
        for i in range(1, n):
            if arr[i] > array[-1]: ## 通过这个来判断当前arr[i]是不是比array里面记录的最长子序列的最后一个元素大.
                ## 如果大的话, 就这样:
                lenth += 1 ## 最长子序列的长度加一
                dp[i] = lenth ## 当前以i位置结尾的arr数组, 最长子序列长度为length
                array.append(arr[i]) ## 然后把arri这个元素加入到array里面. 目前array[-1]就是当前最长子序列的最后一个元素.
            else: ## 如果没有更大的话, 就酱紫:
                index = bisect.bisect(array, arr[i]) ## 去找这个arr[i]应该在array的哪一个位置.
                ## bisect.bisect的原理是什么? 就是寻找在array中, 元素"arr[i]"应该放在哪一个位置. 本质上就是, 如果array[j]比arr[i]小, arr[i]就应当往后挪动, j++, 直到找到一个合适的位置.
                dp[i] = index + 1 ## 更新dp数组. 原理其实挺简单的.
                array[index] = arr[i] ## 修改array本身, 这一步有助于获得字典序更小的子序列.
        res = []
        max_num = array[-1] ## array数组到此, 只有最后一个元素有用, 其他的元素都可以舍弃了.
        max_num_index = arr.index(max_num) ## 寻找max_num在arr中的位置. 也就是说啊, 这个最长子序列应当以这个数字结尾.
        lenth = max(dp) ## max_num这个数字对应的dp[?]肯定就是最长的子序列长度.
        for i in range(max_num_index, -1, -1): ## 倒着遍历, 找到一个递减序列
            if res == [] or (arr[i] < res[-1] and dp[i] == lenth): ## 这个筛选条件是原装的, 不需要整花活了.
                res.append(arr[i])
                lenth -= 1
        return res[::-1] ## 把这个递减序列逆序, 就是递增序列了.

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
print(s.LIS([1, 100, 99, 98, 2, 3, 4, 5]))#[2,1,5,3,6,4,8,9,7]
# print(
#     bisect.bisect([2,1,5,3,6,4,8,9,7], 3)
# )