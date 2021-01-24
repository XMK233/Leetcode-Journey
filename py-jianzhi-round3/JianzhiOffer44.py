'''
[剑指 Offer 44. 数字序列中某一位的数字 - 力扣（LeetCode）](https://leetcode-cn.com/problems/shu-zi-xu-lie-zhong-mou-yi-wei-de-shu-zi-lcof)

数字以0123456789101112131415…的格式序列化到一个字符序列中。在这个序列中，第5位（从下标0开始计数）是5，第13位是1，第19位是4，等等。

请写一个函数，求任意第n位对应的数字。

 

示例 1：

输入：n = 3
输出：3


示例 2：

输入：n = 11
输出：0

 

限制：


	0 <= n < 2^31


注意：本题与主站 400 题相同：https://leetcode-cn.com/problems/nth-digit/
'''
'''
这是辅助代码，可以让你知道每一位对应的数字是什么。
s = ""
for i in range(1000):
    s += str(i)

for i, c in enumerate(s):
    print(i, c)'''

'''
# https://blog.csdn.net/mabozi08/article/details/88904400
## 其实答案里面的解析已经很清楚了。就那样理解好了。就是找规律啦。
## 规律大概可以理解，但是代码没看。直接抄了。
/*
* 这么理解：1~9 有9位，10~99共占180位，100~999共占2700位。
* 目标值是第1001个数。
* 好，1001-9-180=812，越过了第一第二区间还超了812位，那就到了三位数区间了。
* 所以812=270*3+2，说明812位是前面有270个完整的三位数，再附带上后面第271个数的第二位。
* 那么，第270个三位数就是369，第271个三位数是370，所以第二位是7，所以完成。
* */
'''

class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<0:
            return -1
        len_number = 1
        while True:
            numbers = 9 * pow(10, len_number-1)  #len_number位的数字有多少个
            if n <= numbers*len_number:
                a = (n-1)/len_number
                b = (n-1)%len_number
                num = pow(10, len_number-1)+a
                for i in range(len_number-1-b):
                    num = num/10
                return int(num%10)
            n = n-len_number*numbers
            len_number+=1
            print("n",n)
        return -1

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