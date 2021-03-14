# -*- coding:utf-8 -*-
'''
https://www.nowcoder.com/practice/76039109dd0b47e994c08d8319faa352?tpId=117&&tqId=37806&&companyId=665&rp=1&ru=/company/home/code/665&qru=/ta/job-code-high/question-ranking


'''
'''
题目描述
一群孩子做游戏，现在请你根据游戏得分来发糖果，要求如下：
1. 每个孩子不管得分多少，起码分到一个糖果。
2. 任意两个相邻的孩子之间，得分较多的孩子必须拿多一些糖果。(若相同则无此限制)
给定一个数组arr代表得分数组，请返回最少需要多少糖果。
[要求]
时间复杂度为On, 空间复杂度为O1
示例1
输入
复制
[1,1,2]
返回值
复制
4
说明
最优分配方案为1,  1，2

思路就是，正着遍历一遍，反着再来一遍。

'''

class Solution:
    def candy(self , arr ):
        if not arr:
            return []
        ## 把所有孩子的糖果数初始化为 1;
        candies = [1] * len(arr)
        ## 先从左往右遍历一遍，如果右边孩子的评分比左边的高，则右边孩子的糖果数更新为左边孩子的 糖果数加 1;
        for i in range(0, len(arr) - 1):
            if arr[i + 1] > arr[i]:
                candies[i + 1] = candies[i] + 1
        ## 再从右往左遍历一遍，如果左边孩子的评分比右边的高，且左边孩子当前的糖果数不大于右边孩子的糖果数，则左边孩子的糖果数更新为右边孩子的糖果数加 1。
        for i in range(len(arr) - 1, 0, -1):
            if arr[i - 1] > arr[i] and candies[i - 1] <= candies[i]:
                candies[i - 1] = candies[i] + 1
        ## 下面的代码是参考别人的，学学吧。
        # for i in range(1, len(arr) - 1):
        #     if arr[-i - 1] > arr[-i] and candies[-i - 1] <= candies[-i]:
        #         candies[-i - 1] = candies[-i] + 1
        ## 完成。
        return sum(candies)
        ## 虽然可以做，但是总的来说会超时。

print(
    Solution().candy([1,1,2])

)