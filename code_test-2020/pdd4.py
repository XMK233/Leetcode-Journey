## n是指从1到n的数.
## m是features的长度.
## 问, 1到n的数字里面, 有哪些是能够被features里面的任意一个整除的.
## 直接暴力解了. 过了5成我擦.
## 更好的解法应该是比如说储存一下中间结果之类的.

n = 10
m = 3
features = [2, 3, 5]

###########
nums = []
for i in range(1, n+1):
    for f in features:
        if i % f == 0 and i not in nums:
            nums.append(i)

print(len(nums))