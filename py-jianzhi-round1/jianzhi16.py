class Solution:
    def myPow(self, x: float, n: int) -> float:
        ## 负数次方，就要倒数
        if n < 0:
            return 1/self.myPow(x, -n)
        ## 零次方，直接返回1
        if n == 0:
            return 1
        ## 1次方，很明了
        elif n == 1:
            return x
        ## 其他次方：
        else:
            if n % 2 != 0: ## 奇数次幂
                # part1= n // 2
                part1 = self.myPow(x, n//2)
                part2 = part1 * x
                return part1 * part2
            else: ## 偶数次幂
                part1 = self.myPow(x, n//2)
                return part1 * part1

print(Solution().myPow(2.0, -2))