import java.util.LinkedList;
class ListNode {
    int val;
    ListNode next;
    ListNode(int x) { val = x; }
}
public class Jianzhi06 {
    public int[] reversePrint(ListNode head) {
        LinkedList<Integer> stack = new LinkedList<Integer>();
        while(head != null) {
            stack.addLast(head.val);
            head = head.next;
        }
        int[] res = new int[stack.size()];
        for(int i = 0; i < res.length; i++)
            res[i] = stack.removeLast();
        return res;
    }
}

//作者：jyd
//链接：https://leetcode-cn.com/problems/cong-wei-dao-tou-da-yin-lian-biao-lcof/solution/mian-shi-ti-06-cong-wei-dao-tou-da-yin-lian-biao-d/
//来源：力扣（LeetCode）
//著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

/*
* 当然可以用递归, 然后得到后面的倒序结果, 然后再把当前的节点的值放到之前得到的倒序结果的后面.
* 不过, 既然这题是简单题, 那为什么不用栈来倒序呢? 呵呵哒.
* */