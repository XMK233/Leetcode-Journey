# -*- coding:utf-8 -*-
'''
https://www.nowcoder.com/practice/eac1c953170243338f941959146ac4bf?tpId=117&&tqId=37810&&companyId=665&rp=1&ru=/company/home/code/665&qru=/ta/job-code-high/question-ranking

题目描述
给定无序数组arr，返回其中最长的连续序列的长度(要求值连续，位置可以不连续,例如 3,4,5,6为连续的自然数）
示例1
输入
复制
[100,4,200,1,3,2]
返回值
复制
4
示例2
输入
复制
[1,1,1]
返回值
复制
1
备注:
1 \leq n \leq 10^51≤n≤10
5

1 \leq arr_i \leq 10^81≤arr
i
​
 ≤10
8

道理是挺简单的，但是参考的这个方案会超时。
'''
class Solution:
    def MLS(self , arr ):
        arr = set(arr)
        ret = 0
        for num in arr:
            if num-1 not in arr:
                cur = num
                cur_ret = 1
                while cur + 1 in arr:
                    cur += 1
                    cur_ret += 1
                    ret = max(ret, cur_ret)
        return ret

print(
    Solution().MLS([100,4,200,1,3,2])
)