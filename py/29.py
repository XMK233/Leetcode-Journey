class Solution:
    def divide(self, dividend, divisor):
        res, flag = 0, 0
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            flag = -1
        dividend = abs(dividend)
        divisor = abs(divisor)
        while(dividend >= divisor):
            n = 0
            while(dividend >= divisor << n):
                n += 1
            res += 1 << (n - 1)
            dividend -= (divisor << (n - 1))
        res = -res if flag < 0 else res
        if res < -2147483648 or res > 2147483647:
            return 2147483647
        return res

### https://blog.csdn.net/L141210113/article/details/88306238
## 因为不能用基本的运算, 那就用位的移动来代替.
## 所谓的复杂度在logn, 其实体现在哪儿呢?
## 就是体现在不断地使用减法和位移(乘除2的倍数)这样的操作.