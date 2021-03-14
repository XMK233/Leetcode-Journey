# -*- coding:utf-8 -*-
'''
https://www.nowcoder.com/practice/5145394607ea4c5f8b25755718bfddba?tpId=117&&tqId=37733&&companyId=665&rp=1&ru=/company/home/code/665&qru=/ta/job-code-high/question-ranking

题目描述
请写出一个高效的在m*n矩阵中判断目标值是否存在的算法，矩阵具有如下特征：
每一行的数字都从左到右排序
每一行的第一个数字都比上一行最后一个数字大
例如：
对于下面的矩阵：
[
    [1,   3,  5,  9],
    [10, 11, 12, 30],
    [230, 300, 350, 500]
]
要搜索的目标值为3，返回true；
示例1
输入
复制
[[1,3,5,9],[10,11,12,30],[230, 300, 350, 500]],3
返回值
复制
true

参考了别人的实现。思路是，从左下角开始找，直到出界为止。
'''
class Solution:
    def searchMatrix(self , matrix , target ):
        # write code here
        m = len(matrix)
        n = len(matrix[0])
        i=0
        j=n-1
        while i<m and j>=0:
            if matrix[i][j]>target:
                j-=1
            elif matrix[i][j]<target:
                i+=1
            else:
                return True
        return False