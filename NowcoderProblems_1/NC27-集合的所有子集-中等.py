# -*- coding:utf-8 -*-
'''
https://www.nowcoder.com/practice/c333d551eb6243e0b4d92e37a06fbfc9?tpId=117&&tqId=37731&&companyId=665&rp=1&ru=/company/home/code/665&qru=/ta/job-code-high/question-ranking

题目描述
现在有一个没有重复元素的整数集合S，求S的所有子集
注意：
你给出的子集中的元素必须按升序排列
给出的解集中不能出现重复的元素
示例1
输入
复制
[1,2,3]
返回值
复制
[[],[1],[2],[3],[1,2],[1,3],[2,3],[1,2,3]]

DFS+回溯算法。

'''


#
#
# @param A int整型一维数组
# @return int整型二维数组
#
class Solution:
    def subsets(self, A):
        A.sort()
        num_value = len(A)
        path, results = [], []

        def dfs(curt_i, num_char):
            results.append(path.copy()) ## 先记录当前的集合paths，然后再拓展这个paths
            for i in range(curt_i, num_char):
                path.append(A[i]) ## 加入一个字符。
                dfs(i + 1, num_char) ## 递归处理。。。
                path.pop() ## 然后把最后一个字符弹出，这就是回溯。

        dfs(0, num_value)
        return results