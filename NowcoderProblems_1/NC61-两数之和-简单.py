# -*- coding:utf-8 -*-
'''
https://www.nowcoder.com/practice/20ef0972485e41019e39543e8e895b7f?tpId=117&&tqId=37756&&companyId=665&rp=1&ru=/company/home/code/665&qru=/ta/job-code-high/question-ranking

题目描述
给出一个整数数组，请在数组中找出两个加起来等于目标值的数，
你给出的函数twoSum 需要返回这两个数字的下标（index1，index2），需要满足 index1 小于index2.。注意：下标是从1开始的
假设给出的数组中只存在唯一解
例如：
给出的数组为 {20, 70, 110, 150},目标值为90
输出 index1=1, index2=2


示例1
输入
复制
[3,2,4],6
返回值
复制
[2,3]


'''
import collections
class Solution:
    def twoSum(self , numbers , target ):
        map = collections.defaultdict(list)
        for i, number in enumerate(numbers):
            map[number].append(i + 1)
        for number in numbers:
            anotherNumber = target - number
            if anotherNumber == number:
                if len(map[number]) == 2:
                    return sorted(map[number])
                else:
                    continue
            else:
                if anotherNumber in map:
                    return sorted(
                        [
                            map[number][0], map[anotherNumber][0]
                        ]
                    )
                else:
                    continue