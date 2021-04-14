# -*- coding:utf-8 -*-
'''
https://www.nowcoder.com/practice/3fed228444e740c8be66232ce8b87c2f?tpId=117&&tqId=37813&&companyId=665&rp=1&ru=/company/home/code/665&qru=/ta/job-code-high/question-ranking

题目描述
给定一个链表，请判断该链表是否为回文结构。
示例1
输入
复制
[1,2,2,1]
返回值
复制
true
备注:
1 \leq n \leq 10^61≤n≤10
6

先遍历一遍, 然后将这个遍历的结果倒序存在栈里面, 然后再遍历链一遍, 看遍历的结果和倒序的结果是否相同.
'''
class Solution:
    def isPail(self , head ):
        # write code here
        stack = []
        p = head
        while p != None:
            stack.insert(0, p.val)
            p = p.next
        p = head
        for i in stack:
            if i != p.val:
                return "false"
            p = p.next
        return "true"

from BuildChainFromList import buildChainFromList
chain = buildChainFromList([1, 2, 3, 3, 2, 1, 2])
print(Solution().isPail(chain))

## 但是按照上述写的程序没法AC, 下述的反倒能. 这就鬼鬼了.
## 下述的思路几乎没有技术含量, 非常好理解.
while True:
    try:
        x=input()[1:-1].split(',')
        end=len(x)-1
        start=0
        while end>start:
            if x[start]==x[end]:
                start +=1
                end -=1
            else:
                print('false')
                break
        else:
            print('true')
    except:
        break
