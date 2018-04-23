/*
其实方法挺简单。就是递归。
思路就是: 2^n = (2^(n/2))^2。然后考虑一下n为单复数的问题。
注意：
x为0的情况，n为负数或者为0都没有意义。当然，没有意义的话是没有输出的，也就是说，所有的测试用例都会是正例。
n若为最小的负整数，那么-n就不是最大的正整数那么简单。
尽量用位运算作为乘除法。
当然还有更好的思路，日后再看。
https://blog.csdn.net/fengbingyang/article/details/12236121
*/
class Solution {
public:
    double myPow(double x, int n)  
    {  
        if(n<0)  
        {  
            if(n==INT_MIN)  
                return 1.0 / (myPow(x,INT_MAX)*x);  
            else  
                return 1.0 / myPow(x,-n);  
        } 
        
        if(n==0)  
            return 1.0;  
        
        double half = myPow(x,n>>1);  
        if(n%2==0)  
            return half*half;  
        else  
            return half*half*x;  
    }  
};