# -*- coding:utf-8 -*-
'''
https://www.nowcoder.com/practice/fe6b651b66ae47d7acce78ffdd9a96c7?tpId=117&&tqId=37778&&companyId=665&rp=1&ru=/company/home/code/665&qru=/ta/job-code-high/question-ranking

字符串全排列.
剑指offer38.
'''
# -*- coding:utf-8 -*-
class Solution:
    def Permutation(self, s):
        def dfs(s):
            ## 如果遍历完了
            if s == "":
                ## 这里有一个坑。
                ## 因为我自始至终只有1个path，所以呢，如果path里面的元素被删除，那么res里面的也是被删除了的。
                ## 因为是传引用的关系。
                ## 所以你需要做的，就是给它复制一份数组加入到res里面去。
                res.append("".join(path))
                return
            ## 如果遍历没完
            alreadyUsedChar = []
            for i in range(len(s)):
                ## 这里的alreadyUsedChar是什么意思？
                ## 其实就是已经访问过的字符的记录。如果一个字符重复了，那就不要再搞了，直接搞没重复过的即可，
                ## DFS算法里面非常常用的判断重复的一个步骤哦。
                if s[i] in alreadyUsedChar:
                    continue
                alreadyUsedChar.append(s[i])

                path.append(s[i])

                tailPart = ""
                headPart = ""
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
        dfs(s)
        return res #sorted(list(set(res)))
