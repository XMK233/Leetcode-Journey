# -*- coding:utf-8 -*-
'''
https://www.nowcoder.com/practice/f23604257af94d939848729b1a5cda08?tpId=117&&tqId=37817&&companyId=665&rp=1&ru=/company/home/code/665&qru=/ta/job-code-high/question-ranking

题目描述
给定一个无序单链表，实现单链表的排序(按升序排序)。
示例1
输入
复制
[1,3,2,4,5]
返回值
复制
{1,2,3,4,5}

暴力求解, 直接用数组排序来处理.
'''
class Solution:
    def sortInList(self , head ):
        # write code here
        tmp = []
        p = head
        while p != None:
            tmp.append(p)
            p = p.next
        tmp.sort(key=lambda x: x.val)
        p = tmp[0]
        for i in range(len(tmp) - 1):
            tmp[i].next = tmp[i + 1]
        tmp[-1].next = None
        return tmp[0]


