# -*- coding:utf-8 -*-
class Replacement:
    def replaceSpace(self, iniString, length):
    # write code here
        return iniString.replace(" ", "%20")

s = Replacement()
print(s.replaceSpace("Mr John Smith", 13))

