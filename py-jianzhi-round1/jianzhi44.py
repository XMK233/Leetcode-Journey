'''
这是辅助代码，可以让你知道每一位对应的数字是什么。
s = ""
for i in range(1000):
    s += str(i)

for i, c in enumerate(s):
    print(i, c)'''

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

# https://blog.csdn.net/mabozi08/article/details/88904400
## 其实答案里面的解析已经很清楚了。就那样理解好了。就是找规律啦。
## 规律大概可以理解，但是代码没看。直接抄了。