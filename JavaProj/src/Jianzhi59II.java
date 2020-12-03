import java.util.LinkedList;
import java.util.Deque;

public class Jianzhi59II {
    // 普通队列
    private Deque<Integer> deque; // = new LinkedList<Integer>();
    // 记录最大值的队列
    private Deque<Integer> maxDeque; // = new LinkedList<Integer>();
    public Jianzhi59II() {
        deque = new LinkedList<Integer>();
        maxDeque = new LinkedList<Integer>();
    }

    public int max_value() {
        //如果为空
        if (maxDeque.isEmpty()) return -1;
        //如果不为空
        return maxDeque.element();
    }

    public void push_back(int value) {
        //第一步自然是将这个value加到普通的队列中咯.
        deque.add(value);
        // 然后看maxQueue
        if (maxDeque.isEmpty())
            maxDeque.add(value);
        else {
            // 如果当前值比目前的max队列末尾的值大, 就把目前的队尾值顶替掉; 直到不满足为止.
            while (!maxDeque.isEmpty()) {
                int lastVal = maxDeque.removeLast();
                if (value > lastVal)
                    continue;
                else
                    maxDeque.add(lastVal);
                    break;
            }
            maxDeque.add(value);
        }
    }

    public int pop_front() {
        //如果为空
        if (deque.isEmpty()) return -1;
        // 如果不为空
        int res = deque.element(), maxRes = maxDeque.element();
        if (maxRes == res)
            maxDeque.removeFirst();
        return deque.removeFirst();
    }

    public static void main(String []args){
        Jianzhi59II s = new Jianzhi59II();

    }
}
