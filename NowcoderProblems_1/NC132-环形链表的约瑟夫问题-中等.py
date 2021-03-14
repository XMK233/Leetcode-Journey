# -*- coding:utf-8 -*-
'''
https://www.nowcoder.com/practice/41c399fdb6004b31a6cbb047c641ed8a?tpId=117&&tqId=37812&&companyId=665&rp=1&ru=/company/home/code/665&qru=/ta/job-code-high/question-ranking

题目描述
编号为1到n的n个人围成一圈。从编号为1的人开始报数1，依次下去，报到m的人离开，问最后留下的一个人，编号是多少？
示例1
输入
复制
5,2
返回值
复制
3
说明
开始5个人 1，2，3，4，5 ，从1开始报数，1->1，2->2编号为2的人离开
1，3，4，5，从3开始报数，3->1，4->2编号为4的人离开
1，3，5，从5开始报数，5->1，1->2编号为1的人离开
3，5，从3开始报数，3->1，5->2编号为5的人离开
最后留下人的编号是3

备注:
1 \leq n, m \leq 100001≤n,m≤10000

剑指offer的62题
'''
class Solution:
    def ysf(self , n , m ):
        # write code here
        l = [i for i in range(n)]
        idx = 0
        while n > 1:
            idx = (idx + m - 1)%n
            del l[idx]
            n -= 1
        return l[0] + 1
