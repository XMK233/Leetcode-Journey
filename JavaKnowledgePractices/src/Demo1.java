public class Demo1 {

    // 类初始化时,会立即加载该对象，线程安全,调用效率高
    private static Demo1 demo1 = new Demo1();

    private Demo1() {
        System.out.println("私有Demo1构造参数初始化");
    }

    public static Demo1 getInstance() {
        return demo1;
    }

    public static void main(String[] args) {
        Demo1 s1 = Demo1.getInstance();
        Demo1 s2 = Demo1.getInstance();
        System.out.println(s1 == s2);
    }
}

//作者：小杰要吃蛋
//链接：https://juejin.cn/post/6844904125721772039
//来源：掘金
//著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。