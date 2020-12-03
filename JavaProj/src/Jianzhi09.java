import java.util.LinkedList;

public class Jianzhi09 {
    LinkedList<Integer> A, B;
    public Jianzhi09() {
        A = new LinkedList<Integer>();
        B = new LinkedList<Integer>();
    }
    public void appendTail(int value) {
        A.addLast(value);
    }
    public int deleteHead() {
        if(!B.isEmpty()) return B.removeLast();
        if(A.isEmpty()) return -1;
        while(!A.isEmpty())
            B.addLast(A.removeLast());
        return B.removeLast();
    }
}

//作者：jyd
//        链接：https://leetcode-cn.com/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof/solution/mian-shi-ti-09-yong-liang-ge-zhan-shi-xian-dui-l-2/
//        来源：力扣（LeetCode）
//        著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

/*
* 道理很简单.
* push的话永远往A里面推.
* 只要B非空, 那么就从B弹出.
* 如果B空了, A非空, 那么就要把A里面的东西给一次性全部灌进B中, 然后再从B中弹出.
* 如果AB皆空, 那就返回-1, 也就是出错了.
* */
