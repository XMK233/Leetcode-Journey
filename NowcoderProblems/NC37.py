'''
https://www.nowcoder.com/practice/69f4e5b7ad284a478777cb2a17fb5e6a?tpId=117&tqId=37737&rp=1&ru=%2Fta%2Fjob-code-high&qru=%2Fta%2Fjob-code-high%2Fquestion-ranking&tab=answerKey

题目描述
给出一组区间，请合并所有重叠的区间。
示例1
输入
复制
[[10,30],[20,60],[80,100],[150,180]]
返回值
复制
[[10,60],[80,100],[150,180]]

'''

class Interval:
    def __init__(self, a=0, b=0):
        self.start = a
        self.end = b

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




s = Solution()
print(s.merge(
        [
            Interval(10, 30),
            Interval(20, 60),
            Interval(80, 100),
            Interval(150, 180),
        ]
))

