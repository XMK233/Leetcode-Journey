'''
题目描述
一个数组A中存有N（N&gt0）个整数，在不允许使用另外数组的前提下，将每个整数循环向右移M（M>=0）个位置，即将A中的数据由（A0 A1 ……AN-1 ）变换为（AN-M …… AN-1 A0 A1 ……AN-M-1 ）（最后M个数循环移至最前面的M个位置）。如果需要考虑程序移动数据的次数尽量少，要如何设计移动的方法？
示例1
输入
复制
6,2,[1,2,3,4,5,6]
返回值
复制
[5,6,1,2,3,4]
备注:
(1<=N<=100,M>=0)

比较简单. 

'''

class Solution:
    def solve(self , n , m , a ):
        actualMoveStepNum = m % len(a) ## 注意这里, 有的时候m会大于a的长度, 这个时候需要取余.
        print(actualMoveStepNum)
        if actualMoveStepNum == 0:
            return a
        else:
            return a[-actualMoveStepNum:] + a[0:len(a) - actualMoveStepNum]

print(
    Solution().solve(6,4,[1, 2])
)