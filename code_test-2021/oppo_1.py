class Solution:
    def ClimbStairs(self , n ):
        if n < 1:
            return 0
        if n == 1:
            return 1
        # write code here
        sum = 0
        for i in range(1, 7):
            if n - i >= 0:
                sum += self.ClimbStairs(n - i)

        if n in [1, 2, 3, 4, 5, 6]:
            sum += 1
        # if n <= 6:
        #
        # else:
        #     return self.ClimbStairs(n - 1) + self.ClimbStairs(n - 2)+ self.ClimbStairs(n - 3) +self.ClimbStairs(n - 4) +self.ClimbStairs(n - 5) +self.ClimbStairs(n - 6)
        return sum

print(Solution().ClimbStairs(4))