# -*- coding:utf-8 -*-
'''
https://www.nowcoder.com/practice/69f4e5b7ad284a478777cb2a17fb5e6a?tpId=117&&tqId=37737&&companyId=665&rp=1&ru=/company/home/code/665&qru=/ta/job-code-high/question-ranking

题目描述
给出一组区间，请合并所有重叠的区间。
请保证合并后的区间按区间起点升序排列。
示例1
输入
复制
[[10,30],[20,60],[80,100],[150,180]]
返回值
复制
[[10,60],[80,100],[150,180]]
'''
class Solution:
    def haveIntersection(self, intv1, intv2):
        if max(intv1.start, intv2.start) <= min(intv1.end, intv2.end):
            return True
        else:
            return False
    def merge(self , intervals):
        if len(intervals) == 0:
            return []
        # write code here
        sortedIntvs = sorted(intervals, key=lambda x: x.start)
        i = 0
        while len(sortedIntvs) > 1 and i <= len(sortedIntvs) - 2:
            if self.haveIntersection(sortedIntvs[i], sortedIntvs[i + 1]):
                sortedIntvs[i].start = min(sortedIntvs[i].start, sortedIntvs[i + 1].start)
                sortedIntvs[i].end = max(sortedIntvs[i].end, sortedIntvs[i + 1].end)
                sortedIntvs.pop(i+1)
            else:
                i+=1
        return sortedIntvs