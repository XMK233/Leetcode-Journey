/*
自己的方法没有去实现。
看了网上攻略，如果用递归的话，可能会超时。
所以得用回溯。
这里采用的非递归回溯法，其实实现起来比较朴素：标记某一个位置，然后在后面进行匹配，如果匹配不成功，那么就重新回到标记的点附近重新开始匹配。
在这道题中，标记的位置是p串中*的位置和s中的某个相应位置，然后逐个匹配s和p后面的字符；
如果遇到不匹配的情况，那就倒回标记附近重新开始逐个匹配，直到s为空。以s为空为循环结束的条件。
如果p为空s不为空，则视同p与s当前字符不匹配。

方法来源：https://blog.csdn.net/makuiyu/article/details/43698963 
*/

bool isMatch(const char *s, const char *p)
    {
        const char *ss = s, *pp = NULL;
        while('\0' != *s)
        {
            if('?' == *p || *s == *p)
                 ++ s, ++ p;
             else if('*' == *p)
                 ss = s, pp = p ++;
             else if(pp != NULL)
                 s = ++ ss, p = pp + 1;
             else
                 return false;
         }

         while('*' == *p)
             ++ p;

         return '\0' == *p;
   }