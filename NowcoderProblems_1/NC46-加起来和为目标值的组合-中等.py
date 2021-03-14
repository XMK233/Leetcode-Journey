# -*- coding:utf-8 -*-
'''
https://www.nowcoder.com/practice/75e6cd5b85ab41c6a7c43359a74e869a?tpId=117&&tqId=37742&&companyId=665&rp=1&ru=/company/home/code/665&qru=/ta/job-code-high/question-ranking

题目描述
给出一组候选数\ C C 和一个目标数\ T T，找出候选数中起来和等于\ T T 的所有组合。
\ C C 中的每个数字在一个组合中只能使用一次。
注意：
题目中所有的数字（包括目标数\ T T ）都是正整数
组合中的数字 (a_1, a_2, … , a_ka
1
​
 ,a
2
​
 ,…,a
k
​
 ) 要按非递增排序 (a_1 \leq a_2 \leq … \leq a_ka
1
​
 ≤a
2
​
 ≤…≤a
k
​
 ).
结果中不能包含重复的组合
组合之间的排序按照索引从小到大依次比较，小的排在前面，如果索引相同的情况下数值相同，则比较下一个索引。
示例1
输入
复制
[100,10,20,70,60,10,50],80
返回值
复制
[[10,10,60],[10,20,50],[10,70],[20,60]]
说明
给定的候选数集是[100,10,20,70,60,10,50]，目标数是80

直接看参考代码吧，是一种回溯算法。

'''
#
#
# @param num int整型一维数组
# @param target int整型
# @return int整型二维数组
#
class Solution:
    def combinationSum2(self , num , target ):
        res = []
        path = []
        def trackBack(target, start):
            if target == 0:
                res.append(path.copy())
                return
            for i in range(start,len(num)):
                if num[i] > target: ## 因为num是被排序了的，所以这里可以之间判断然后断开。
                    break
                if i > start and num[i] == num[i - 1]: ## 跳过重复的数字。
                    continue
                path.append(num[i]) ## 加入进去
                trackBack(target - num[i],i + 1)
                path.pop() ## 弹出，也就是回溯了。
        num.sort()
        trackBack(target, 0)
        return res