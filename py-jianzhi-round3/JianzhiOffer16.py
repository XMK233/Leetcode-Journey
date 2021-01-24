'''
[剑指 Offer 16. 数值的整数次方 - 力扣（LeetCode）](https://leetcode-cn.com/problems/shu-zhi-de-zheng-shu-ci-fang-lcof)

实现函数double Power(double base, int exponent)，求base的exponent次方。不得使用库函数，同时不需要考虑大数问题。

 

示例 1:

输入: 2.00000, 10
输出: 1024.00000


示例 2:

输入: 2.10000, 3
输出: 9.26100


示例 3:

输入: 2.00000, -2
输出: 0.25000
解释: 2-2 = 1/22 = 1/4 = 0.25

 

说明:


	-100.0 < x < 100.0
	n 是 32 位有符号整数，其数值范围是 [−231, 231 − 1] 。


注意：本题与主站 50 题相同：https://leetcode-cn.com/problems/powx-n/
'''

'''
递归分治. 道理比较简单. 
'''
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
                ## 这里是一个小技巧. 就是只递归求半边的结果, 然后把半边的结果自乘积.
                ## 如果两半边都拿来递归, 就起不到省力的效果了.
                return part1 * part2
            else: ## 偶数次幂
                part1 = self.myPow(x, n//2)
                return part1 * part1

print(Solution().myPow(2.0, -2))

##-----------------------------------------------------------------------------

import os, sys, re
selfName = os.path.basename(sys.argv[0])
id = selfName.replace("JianzhiOffer", "").replace(".py", "")
# id = "57"

round1_dir = "C:/Users/XMK23/Documents/Leetcode-Journey/py-jianzhi-round1"
for f in os.listdir(round1_dir):
    if ".py" not in f:
        continue
    num = re.findall("\d+-*I*", f)
    if len(num) == 0:
        continue
    id_ = num[0]
    if id == id_:
        with open(os.path.join(round1_dir, f), "r", encoding="utf-8") as rdf:
            lines = rdf.readlines()
            print(f)
            print("".join(lines))
            print()