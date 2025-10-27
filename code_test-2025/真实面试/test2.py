import re

keyboard = {
    '2':'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz'
}

rst = []

def get_combination(s):
    if s is None:
        return []
    if len(s) == 1:
        return list(keyboard[s])
    rst_last = get_combination(s[1:])
    rst_here = []
    for xx in keyboard[s[0]]:
        for yy in rst_last:
            rst_here.append(xx + yy)
    return rst_here
# print(get_combination("345"))


class Solution:
    def can_jump(self, nums):
        # write code here
        far_place = 0
        for idx in range(len(nums)):
            if idx > far_place:
                return False
            far_place = max(far_place, idx + nums[idx])
            if far_place >= (len(nums)-1):
                return True
        if far_place >= (len(nums)-1):
            return True
        else:
            return False

nums = [2,3,1,1,4] # [0] #[2,3,1,0,0,5]
## 要测一测[0]是不是True
# print(
#     Solution().can_jump(nums)
# )


import re
class Solution:
    def add_tags(self, words, s) :
        n = len(s)
        bold = [False]*n
        for word in words:
            length = len(word)
            for i in range(n-length+1):
                if s[i:i+length] == word:
                    for j in range(i, i+length):
                        bold[j]=True
        result = []
        i = 0
        while i < n:
            if bold[i]:
                result.append("<bold>")
                while i < n and bold[i]:
                    result.append(s[i])
                    i+=1
                result.append("</bold>")
            else:
                result.append(s[i])
                i += 1
        return "".join(result)





words, s = ["abc","old"],"abc123"
print(
    Solution().add_tags(words, s)
)






