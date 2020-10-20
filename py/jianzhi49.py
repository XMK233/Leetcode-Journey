class Solution:
    def nthUglyNumber(self, n: int) -> int:
        UglyList = [1]
        index2 = 0
        index3 = 0
        index5 = 0
        for i in range(n-1):
            newUgly = min(UglyList[index2]*2, UglyList[index3]*3, UglyList[index5]*5)
            UglyList.append(newUgly)
            if newUgly%2==0:
                index2+=1
            if newUgly%3 == 0:
                index3+=1
            if newUgly%5 == 0:
                index5+=1
        return UglyList[-1]

## https://blog.csdn.net/mabozi08/article/details/88938205
## 丑数. 算法其实还算是很简单的.
## index2, index3, index5指的是, UglyList的这个位置上的数字应该乘以2, 3, 5.
## 然后, 把三个index指的数字分别乘以相应的2/3/5, 得到三个积, 从这三个积中得到最小的数字, 就是当前最新的丑数, 加入到UglyList列表中.
## 然后, 最新的丑数是通过哪个index得到的, 这个index就自增1. 同时, 如果最新的丑数还是另外两个数中某一个或两个的倍数, 那么对应的index也要自增1.
## 就是这么骚. 其实大概的流程, 自己试着跑一下, 能出来的, 也很容易理解.