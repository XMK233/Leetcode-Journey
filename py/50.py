class Solution(object):
    def myPow(self, x, n):
        if n == 0:
            return 1
        if n == 1:
            return x
        if n < 0:
            return 1/(self.myPow(x, n*-1))
        #递归x与n的一半
        half = self.myPow(x, int(n/2))
        #如果是偶数就递归0，奇数就递归1，意思就是奇数多乘一个x
        rem = self.myPow(x, n%2)
        return half *half * rem

### https://blog.csdn.net/L141210113/article/details/88614600
### 其实思路也很简单. 就是递归嘛. 先求一半的积, 然后再乘起来, 就是全部的结果了.
### 考虑大于1, 等于1, 小于1的各种情况.