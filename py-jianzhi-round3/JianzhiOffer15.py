'''
[剑指 Offer 15. 二进制中1的个数 - 力扣（LeetCode）](https://leetcode-cn.com/problems/er-jin-zhi-zhong-1de-ge-shu-lcof)

请实现一个函数，输入一个整数（以二进制串形式），输出该数二进制表示中 1 的个数。例如，把 9 表示成二进制是 1001，有 2 位是 1。因此，如果输入 9，则该函数输出 2。

 

示例 1：

输入：00000000000000000000000000001011
输出：3
解释：输入的二进制串 00000000000000000000000000001011 中，共有三位为 '1'。


示例 2：

输入：00000000000000000000000010000000
输出：1
解释：输入的二进制串 00000000000000000000000010000000 中，共有一位为 '1'。


示例 3：

输入：11111111111111111111111111111101
输出：31
解释：输入的二进制串 11111111111111111111111111111101 中，共有 31 位为 '1'。

 

提示：


	输入必须是长度为 32 的 二进制串 。


 

注意：本题与主站 191 题相同：https://leetcode-cn.com/problems/number-of-1-bits/
'''
'''
# 作者：jyd
# 链接：https://leetcode-cn.com/problems/er-jin-zhi-zhong-1de-ge-shu-lcof/solution/mian-shi-ti-15-er-jin-zhi-zhong-1de-ge-shu-wei-yun/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

比较简单得做法是: n与1相与, 就知道最后一位是不是1; 然后n右移一位, 重复上述流程, 直到n变成0. 复杂度取决于n最高位1在第几位. 对吧. 
更酷炫一点的做法就是: n与n-1相与, 就会自动消掉最右边的1, 然后n变成上一步相与的结果, 重复本流程, 直到n变成0. 复杂度直接取决于1的个数. 
'''
class Solution:
    def hammingWeight(self, n: int) -> int:
        ## 酷炫法
        res = 0
        while n:
            ## 每做一次这个, 就自动消掉了一个1.
            n = n & (n - 1)
            res += 1
        ## 简单做法
        # res = 0
        # while n:
        #     res += n & 1
        #     n >>= 1

        return res

s = Solution()
print(s.hammingWeight(0))

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