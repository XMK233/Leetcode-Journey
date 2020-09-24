'''
在小美的国家，任何一篇由英文字母组成的文章中，如果大小写字母的数量不相同会被认为文章不优雅。
现在，小美写了一篇文章，并且交给小团来修改。小美希望文章中的大小写字母数量相同，所以她想让小团帮她把某些小写字母改成对应的大写字母，或者把某些大写字母改成对应的小写字母，使得文章变得优雅。
小美给出的文章一定是由偶数长度组成的，她想知道最少修改多少个字母，才能让文章优雅。
'''
string = input()
upperCount = 0
lowerCount = 0
for c in string:
    if c.isupper():
        upperCount += 1
    # else:
    #     lowerCount += 1
print(abs(len(string) // 2 - upperCount))