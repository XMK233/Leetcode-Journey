class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        sign = 1 if numerator*denominator >= 0 else -1
        numerator = abs(numerator)
        denominator = abs(denominator)
        numeratorlist = []
        valuelist = []
        indexValue = -1
        div,mod = divmod(numerator, denominator)
        if mod == 0:
            return str(div * sign)
        valuelist.append(div)
        valuelist.append(".")
        mod = mod * 10
        while True:
            numeratorlist.append(mod)
            div,mod = divmod(mod, denominator)
            valuelist.append(div)
            mod = mod * 10
            if mod in numeratorlist:
                indexValue = numeratorlist.index(mod) + 2 #因为list已经添加了整数部分（一个数）和“.”
                break
            if mod == 0:
                break
        if indexValue != -1:
            valuelist.append(")")
            valuelist.insert(indexValue,"(")
        if (sign < 0):
            valuelist.insert(0,"-")
        resultStr = ''.join(map(str,valuelist))
        return resultStr

# s = Solution()
# print(s.fractionToDecimal(5, 7))

### https://blog.csdn.net/ch717828/article/details/44061303
## 首先, 基本的除法, 我已经忘了要怎么做了. 呵呵, 二年级的知识了.
## 只要把小学的知识回想一下, 然后用普通的厂字形除法, 严格实现一遍, 就完全够用了.