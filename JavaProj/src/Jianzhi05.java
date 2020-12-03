public class Jianzhi05 {
    public String replaceSpace(String s) {
        StringBuilder res = new StringBuilder();
        for(Character c : s.toCharArray())
        {
            if(c == ' ') res.append("%20");
            else res.append(c);
        }
        return res.toString();
    }
}

//作者：jyd
//链接：https://leetcode-cn.com/problems/ti-huan-kong-ge-lcof/solution/mian-shi-ti-05-ti-huan-kong-ge-ji-jian-qing-xi-tu-/
//来源：力扣（LeetCode）
//著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

// 最直观也是最有效的做法就是, 遍历, 每碰到一个空格, 就标注, 这里换成%20.
// 其实还有一种原地修改的方法, 可以进一步降低空间复杂度:
/*
* 原来的数组边长, 也就是, 把所有的空格替换为%20之后, 会有多长, 就把原数组延长到这么长.
* 然后, 倒着遍历, 把字符挪到后面去, 然后碰到空格, 就倒着加入0, 2, %就行了.
* */
