# -*- coding:utf-8 -*-
'''
https://www.nowcoder.com/practice/a43a2b986ef34843ac4fdd9159b69863?tpId=117&&tqId=37739&&companyId=665&rp=1&ru=/company/home/code/665&qru=/ta/job-code-high/question-ranking

题目描述
给出一组可能包含重复项的数字，返回该组数字的所有排列。
示例1
输入
复制
[1,1,2]
返回值
复制
[[1,1,2],[1,2,1],[2,1,1]]

NC43的实现已经OK了，也就是剑指offer38的实现，也可以应对有重复数字的情况。
'''
#
#
# @param num int整型一维数组
# @return int整型二维数组
#
class Solution:
    def permuteUnique(self, nums):
        def dfs(s):
            ## 如果遍历完了
            if s == []:
                ## 这里有一个坑。
                ## 因为我自始至终只有1个path，所以呢，如果path里面的元素被删除，那么res里面的也是被删除了的。
                ## 因为是传引用的关系。
                ## 所以你需要做的，就是给它复制一份数组加入到res里面去。
                res.append(path.copy())
                return
            ## 如果遍历没完
            alreadyUsedNums = []
            for i in range(len(s)):
                ## 这里的alreadyUsedChar是什么意思？
                ## 其实就是已经访问过的字符的记录。如果一个字符重复了，那就不要再搞了，直接搞没重复过的即可，
                ## DFS算法里面非常常用的判断重复的一个步骤哦。
                if s[i] in alreadyUsedNums:
                    continue
                alreadyUsedNums.append(s[i])

                path.append(s[i])

                tailPart = []
                headPart = []
                if i == 0:
                    tailPart = s[1:]
                elif i == len(s) - 1:
                    headPart = s[0:i]
                else:
                    headPart = s[0:i]
                    tailPart = s[i + 1:]
                s1 = headPart + tailPart
                dfs(s1)
                path.pop(-1) ## 这里当时写错了，写程remove(s[i])这样会把很多无辜的元素删掉。
            return

        res = []
        path = []
        dfs(nums)
        return res #sorted(list(set(res)))
