#利用hash表；还有就是一定要想到好的测试用例。"tmmzuxt"和"abcabcbb"这两种测试用例说明了两种情况。
#
#Python。
#
#关键点：只需遍历一遍就行了。不要硬性穷举。
#利用hash表来判断字符是否重复，用空间换时间。
#如果发现有一个字符重复出现了，那么新的最大子串只可能从（重复的字符上一次出现的地方的后一个地方，这个地方我们称为head）开始。
#如果head之后遍历到一个重复字符串重复了，但是上一次这个字符串出现的位置在head之前，
#那么就说明这个“重复字符”实际上并不是真正的重复字符，应当作为新出现的字符来看待，只
#要像普通字符串那样更新就好了。



class Solution:
    def lengthOfLongestSubstring1(self, s):
        """
        :type s: str
        :rtype: int
        """
        head = 0
        longest = 0
        dic = {}#存放的是字符，以及字符在字符串中的序号。
        for i in range(len(s)):
            if s[i] not in dic: #如果这个字符是新的  
                dic[s[i]] = i #那就只顾着加进字典里就行了，键是字符，值是此时这个字符出现的序号
            else: #否则，
                if dic[s[i]] >= head: #如果出现重复的字符在head所指字符之后或者就是head所指字符
                    head = dic[s[i]] + 1  #那新的head就是重复字符的下一个字符。
                dic[s[i]] = i #无论是出现在之后还是之前，总之都要更新这个重复字符的序号
            
            longest = (i - head + 1) if (i - head + 1) > longest else longest  #看看最大长度有没有更新
            
        return longest
    
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        head = 0
        longest = 0
        dic = {}#存放的是字符，以及字符在字符串中的序号。
        
        for i in range(len(s)):
            if s[i] in dic and dic[s[i]] >= head: #如果这个字符是重复的字符，并且上一次出现在head之后，
                head = dic[s[i]] + 1 #才需要移动head
            dic[s[i]] = i #否则一律按新出现字符来看待。
            longest = (i - head + 1) if (i - head + 1) > longest else longest  #看看最大长度有没有更新
            
        return longest