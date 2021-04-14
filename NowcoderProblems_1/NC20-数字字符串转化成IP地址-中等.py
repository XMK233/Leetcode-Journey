# -*- coding:utf-8 -*-
'''
https://www.nowcoder.com/practice/ce73540d47374dbe85b3125f57727e1e?tpId=117&&tqId=37725&&companyId=665&rp=1&ru=/company/home/code/665&qru=/ta/job-code-high/question-ranking

题目描述
现在有一个只包含数字的字符串，将该字符串转化成IP地址的形式，返回所有可能的情况。
例如：
给出的字符串为"25525522135",
返回["255.255.22.135", "255.255.221.35"]. (顺序没有关系)
示例1
输入
复制
"25525522135"
返回值
复制
["255.255.22.135","255.255.221.35"]

一个典型的回溯套路. 参考了已经通过的思路.
'''


class Solution:
    def restoreIpAddresses(self, s):
        # write code here
        res = []
        def backtrack(track, start, s):
            # 满四段且用光所有字符串
            if len(track) == 4 and start == len(s):
                res.append('.'.join(track))
            # 满四段但没用光所有字符串
            if len(track) == 4 and start < len(s):
                return

            for l in range(1, 4): ## 这里的l是指, 从start开始的子串长度为l. 比如如果l为2, 那么从start开始的子串就是start和它后面那一个字符组成的.
                # 字符不存在,超出边界，最后一个字符的索引为s[start + l - 1]
                if start + l - 1 >= len(s):
                    return
                # 若选择长度超过1的字串，则不能是'0'开头
                if l >= 2 and s[start] == "0":
                    return
                tmp = s[start:start + l]
                # 长度为3的字串，取值不能大于225
                if l == 3 and int(tmp) > 255:
                    return
                backtrack(track + [tmp], start + l, s) ## 这里就体现回溯了, 因为当tmp换掉了之后, track还是没变啊, 只是把track+[tmp]给送到后面的递归去了.

        backtrack([], 0, s)
        return res