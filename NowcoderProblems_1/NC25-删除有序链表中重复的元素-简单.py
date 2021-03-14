# -*- coding:utf-8 -*-
'''
https://www.nowcoder.com/practice/c087914fae584da886a0091e877f2c79?tpId=117&&tqId=37730&&companyId=665&rp=1&ru=/company/home/code/665&qru=/ta/job-code-high/question-ranking

题目描述
删除给出链表中的重复元素（链表中元素从小到大有序），使链表中的所有元素都只出现一次
例如：
给出的链表为1\to1\to21→1→2,返回1 \to 21→2.
给出的链表为1\to1\to 2 \to 3 \to 31→1→2→3→3,返回1\to 2 \to 31→2→3.

示例1
输入
复制
{1,1,2}
返回值
复制
{1,2}

比较简单，直接看代码吧。

'''
#
#
# @param head ListNode类
# @return ListNode类
#
class Solution:
    def deleteDuplicates(self , head ):
        # write code here
        if not head:
            return None
        myhead=head
        while myhead.next:
            if myhead.val==myhead.next.val:
                myhead.next=myhead.next.next
            else:
                myhead=myhead.next
        return head