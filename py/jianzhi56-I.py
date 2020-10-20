class Solution:
    def singleNumbers(self, nums):
        ret = 0 ## 这个就是总异或结果
        a = 0
        b = 0
        for n in nums:
            ret ^= n
        ## 找ret里面第一个不是0的位, 也就是这个h
        h = 1
        while (h & ret == 0):
            h <<= 1
        ##
        for num in nums:
            if num & h:
                a ^= num
            else:
                b ^= num
        return [a, b]

## https://leetcode-cn.com/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-lcof/solution/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-by-leetcode/
## 道理是酱紫的. 假设能够配对的数字被称为对子, 两个落单的都是单身狗,
## 那么第一步, 先将所有的数字都异或起来, 得到的结果其实本质上就是单身狗之间异或的结果.
## 第二步, 将单身狗异或结果当中随便挑一个非0的位, 这个位上, 俩单身狗, 其中一个必为1, 另一个必为0.
## 所以, 将这一位上为1的数字归为一类, 为0的归为一类.
## 这么做能确保配对的两个数字必然会在同一个类里面, 而俩单身狗必定会被分开.
## 然后两个类里面, 就只有一个单身狗了, 所以第三步就是在每一个类别里面进行总异或, 得到的结果就是两个单身狗的值了.