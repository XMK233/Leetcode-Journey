# -*- coding:utf-8 -*-
'''
https://www.nowcoder.com/practice/89865d4375634fc484f3a24b7fe65665?tpId=117&&tqId=37727&&companyId=665&rp=1&ru=/company/home/code/665&qru=/ta/job-code-high/question-ranking

题目描述
给出两个有序的整数数组 A和 B，请将数组 B合并到数组 A中，变成一个有序的数组
注意：
可以假设 A数组有足够的空间存放 B数组的元素， A和 B中初始的元素数目分别为 m和n

这里的技巧是, 倒着遍历AB两个数组. 这样不要反复多次的遍历和挪动.
'''
class Solution:
    def merge(self , A, m, B, n):
        # write code here
        p0=m-1
        p1=n-1
        p=m+n-1
        while p0>=0 and p1>=0:
            if A[p0]<=B[p1]:
                A[p]=B[p1]
                p1-=1
            else:
                A[p]=A[p0]
                p0-=1
            p-=1
        A[:p1+1]=B[:p1+1]