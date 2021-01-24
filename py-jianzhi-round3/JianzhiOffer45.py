'''
[剑指 Offer 45. 把数组排成最小的数 - 力扣（LeetCode）](https://leetcode-cn.com/problems/ba-shu-zu-pai-cheng-zui-xiao-de-shu-lcof)

输入一个非负整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。

 

示例 1:

输入: [10,2]
输出: "102"

示例 2:

输入: [3,30,34,5,9]
输出: "3033459"

 

提示:


	0 < nums.length <= 100


说明: 


	输出结果可能非常大，所以你需要返回一个字符串而不是整数
	拼接起来的数字可能会有前导 0，最后结果不需要去掉前导 0

'''
'''
# https://blog.csdn.net/mabozi08/article/details/88929407
## 这道题的精髓在于怎么比两个字符串的大小.
### 即: a, b两个字符串, 如果a+b > b+a, 那么a就大于b.
## 得到了字符串比较大小的方法, 就可以利用这种大小关系进行排序, 把小的放到前面就行了.
## 这里利用了一个内置的库, 对数组实行自定义排序.
### 目测, 只要函数f(a, b)满足, 如果a >= b 返回1, 否则返回-1就可以被使用.
'''

import functools
class Solution:
    def minNumber(self, nums):
        # write code here
        if not nums:
            return ""
        arr = list(str(x) for x in nums)
        def f(a,b):
            if a+b<b+a:
                return -1
            else:
                return 1
        arr.sort(key=functools.cmp_to_key(f))
        return int("".join(arr))

s = Solution()
print(s.minNumber([2, 10]))

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