/*
从这里开始，只要不特别说明，那么我就是用java做的。
如果用两重循环，那么一定能够算出来，时间复杂度就是O(n)。
有一些技巧，比如说，指针分别指向头尾，然后看看体积是不是当前最大的，如果是就记录。
无论是否是最大的，我们都要移动指针，比如说，头指针指向的高度比尾指针的矮，那么头指针后移，否则尾指针前移。
就是如此。
*/

class Solution {
    public int maxArea(int[] height){
        //height's length is at least 2;
        //consider that situation: length is exactly the 2;
        int head = 0, tail = height.length - 1;
        int maxCap = 0;
        while(head < tail) {
            /*int temp = (tail - head) * height[head] > height[tail] ? height[tail] : height[head];
            if (temp > maxCap) maxCap = temp;
            if (height[head] )*/
            if (height[head] > height[tail]) {
                int temp = (tail - head) * height[tail];
                if (temp > maxCap) maxCap = temp;
                tail--;
            }
            else {
                int temp = (tail - head) * height[head];
                if (temp > maxCap) maxCap = temp;
                head++;
            }

        }
        return maxCap;
    }
}