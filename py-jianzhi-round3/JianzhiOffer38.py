'''
[剑指 Offer 38. 字符串的排列 - 力扣（LeetCode）](https://leetcode-cn.com/problems/zi-fu-chuan-de-pai-lie-lcof)

输入一个字符串，打印出该字符串中字符的所有排列。

 

你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。

 

示例:

输入：s = "abc"
输出：["abc","acb","bac","bca","cab","cba"]


 

限制：

1 <= s 的长度 <= 8
'''

'''
以前的实现呢，使用的是递归。比较麻烦。
现在做了一些改进。
最明显的改动，就是使用了的dfs方法。我记得有一次面试，就是问的这个问题。
后来面试官说，更好的方法是使用dfs啥的方法。
这不就试一试嘛。结果还行诶。
'''

class Solution:
    def permutation(self, s):
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

s = Solution()
print(s.permutation("aaabc"))

import itertools
st = ["".join(tpl) for tpl in itertools.permutations("aaabc")]
print(sorted(list(set(st))))
##-----------------------------------------------------------------------------

# import os, sys, re
# selfName = os.path.basename(sys.argv[0])
# id = selfName.replace("JianzhiOffer", "").replace(".py", "")
# # id = "57"
#
# round1_dir = "C:/Users/XMK23/Documents/Leetcode-Journey/py-jianzhi-round1"
# for f in os.listdir(round1_dir):
#     if ".py" not in f:
#         continue
#     num = re.findall("\d+-*I*", f)
#     if len(num) == 0:
#         continue
#     id_ = num[0]
#     if id == id_:
#         with open(os.path.join(round1_dir, f), "r", encoding="utf-8") as rdf:
#             lines = rdf.readlines()
#             print(f)
#             print("".join(lines))
#             print()