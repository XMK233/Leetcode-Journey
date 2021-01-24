'''
[剑指 Offer 17. 打印从1到最大的n位数 - 力扣（LeetCode）](https://leetcode-cn.com/problems/da-yin-cong-1dao-zui-da-de-nwei-shu-lcof)

输入数字 n，按顺序打印出从 1 到最大的 n 位十进制数。比如输入 3，则打印出 1、2、3 一直到最大的 3 位数 999。

示例 1:

输入: n = 1
输出: [1,2,3,4,5,6,7,8,9]


 

说明：


	用返回一个整数列表来代替打印
	n 为正整数

'''

'''
# 作者：jyd
# 链接：https: // leetcode - cn.com / problems / da - yin - cong - 1
# dao - zui - da - de - nwei - shu - lcof / solution / mian - shi - ti - 17 - da - yin - cong - 1 - dao - zui - da - de - n - wei - 2 /
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

这个问题本质上是用数组或者是字符串来表示大数字. 
dfs的思路更加符合问题的本质. 应当好好体悟一下. 
因为python支持大整数, 所以反倒没必要使用dfs了. 直接掰指头数(a.k.a 普通递归), 都能把这个问题很快求解. 
'''
class Solution:
    def printNumbers(self, n: int) -> [int]:
        def dfs(x: int, leadingZero: bool):
            if x == n:  # 终止条件：已固定完所有位
                res.append(''.join(num))  # 拼接 num 并添加至 res 尾部
                return
            for i in range(10):  # 遍历 0 - 9
                ## 有起始0, 就不要加进新的0了, 没意义.
                if i == 0 and leadingZero:
                    dfs(x + 1, True)  # 开启固定第 x + 1 位
                else:
                    num[x] = str(i)  # 固定第 x 位为 i
                    dfs(x + 1, False)  # 开启固定第 x + 1 位

        num = [''] * n  # 起始数字定义为 n 个 0 组成的字符列表
        res = []  # 数字字符串列表
        dfs(0, True)  # 开启全排列递归
        res.remove("")
        return [int(_) for _ in res] #','.join(res)  # 拼接所有数字字符串，使用逗号隔开，并返回

s = Solution()
print(len(s.printNumbers(2)))

'''
这就是所谓的python普通递归法. 
'''
# class Solution:
#     def printNumbers(self, n: int) -> List[int]:
#         res = []
#         for i in range(1, 10 ** n):
#             res.append(i)
#         return res
#
# # 作者：jyd
# # 链接：https://leetcode-cn.com/problems/da-yin-cong-1dao-zui-da-de-nwei-shu-lcof/solution/mian-shi-ti-17-da-yin-cong-1-dao-zui-da-de-n-wei-2/
# # 来源：力扣（LeetCode）
# # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
#
# ## 没什么可说的了。很简单。

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