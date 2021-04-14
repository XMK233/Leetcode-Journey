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

## 之前之所以没有AC估计是因为class 外的部分写得不太对. 什么玩意儿.
class Solution:
    def MLS(self, arr):
        s = set(arr)
        ans = 0
        for i in s:
            if i - 1 not in s: ## 这里说明啥呢? 说明一个连续序列以它为头, 比如示例1的"1", 就是"1234"这个序列的头一个.
                ## 如果你后来遇上了2, 那么2-1=1, 1在s中, 也就是说2不是一个连续序列的开头, 那就跳过好了.
                cur = i
                len_cur = 1
                while cur + 1 in s: ## 只要找到了一个开头, 就在s中找后续的值. 直到找不到为止.
                    cur += 1
                    len_cur += 1
                ans = max(ans, len_cur)
        return ans


s = Solution()
while True:
    try:
        arr = list(map(int, input()[1:-1].split(',')))
        print(s.MLS(arr))
    except:
        break