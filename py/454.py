## 蛮力解是n的四次方, 能给他优化成n平方.
## 道理也就文明了一点点, 不过就是先蛮力求解两个数组的和, 然后再看另两个数组的和有没有
## 能够配套的, 如果有, 就多了一个目标元组.
## 呵呵哒. 我真是无语了. 竟然可以这么玩. 这么玩也叫优化? 太对不起我的期待了.

class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        # use hashtable to store the number and count
        h = {}
        for a in A:
            for b in B:
                h[a + b] = h.get(a + b, 0) + 1

        count = 0
        for c in C:
            for d in D:
                if -(c + d) in h:
                    count += h[-(c + d)]
        return count

# https://blog.csdn.net/danspace1/article/details/86062583