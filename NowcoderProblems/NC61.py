'''
https://www.nowcoder.com/practice/20ef0972485e41019e39543e8e895b7f?tpId=117&tqId=37756&rp=1&ru=%2Fta%2Fjob-code-high&qru=%2Fta%2Fjob-code-high%2Fquestion-ranking&tab=answerKey

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

我自己的方法就是twoSum1, 非常费事, 一直错, 一直调才对, 说明这种思路不好. 时间复杂度也很高, 因为排序了很多次; 空间复杂度也不低, 因为中途复制了几次数组.

所以我们这时反倒可以回到最简单的方法去做这道题. https://blog.nowcoder.net/n/d6872cb4c0cb46ad9bdbe26a3941ac2d

'''
import collections

class Solution:
    def twoSum1(self, numbers, target):
        def findIndices(index1, index2):
            idx1 = numbers.index(num[index1])
            if num[index1] == num[index2]:
                idx2 = numbers.index(num[index2], idx1 + 1)
            else:
                idx2 = numbers.index(num[index2])
            return sorted([idx1 + 1, idx2 + 1])
        num = sorted(numbers)
        ##
        index1 = 0
        index2 = len(num) - 1

        while index1 < index2:
            if num[index1] + num[index2] < target:
                index1 += 1
            elif num[index1] + num[index2] > target:
                index2 -= 1
            else:
                return findIndices(index1, index2)

    def twoSum(self , numbers , target ):
        map = collections.defaultdict(list)
        for i, number in enumerate(numbers):
            map[number].append(i + 1)
        for number in numbers:
            anotherNumber = target - number ## 另一半的是哪个数字.
            if anotherNumber == number:
                if len(map[number]) == 2: ## 如果number出现两次, 那么直接返回就好了.
                    return sorted(map[number])
                else: ## 否则, number就不是正确答案, 得找其他组合.
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

s = Solution()
print(s.twoSum([3,2,4],6))