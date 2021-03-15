# -*- coding:utf-8 -*-
'''
https://www.nowcoder.com/practice/e297fdd8e9f543059b0b5f05f3a7f3b2?tpId=117&&tqId=37852&&companyId=665&rp=1&ru=/company/home/code/665&qru=/ta/job-code-high/question-ranking

判断一个字符串全文是不是回文. 用python写是相当容易的.
'''
class Solution:
    def judge(self , str ):
        # write code here
        input_str = str
        new_str = input_str[::-1]
        if new_str == input_str:
            return True
        else:
            return False