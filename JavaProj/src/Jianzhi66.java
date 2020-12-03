public class Jianzhi66 {
    public int[] constructArr(int[] a) {
        // 先行获得左边积列表.
        int [] leftProducts = new int[a.length];
        for (int p = 1, i = 0; i < a.length; i++){
            p *= a[i];
            leftProducts[i] = p;
        }
        // 然后右边积无需列表, 仅以一数做记录即可. 该数以1始.
        for (int i = a.length - 1, rightProduct = 1; i >= 0; i--){
            // 反向遍历左边积列表. 先得左边积, 将其乘以右边积, 得目前值, 然后更新右边积(原右边积乘以当前值).
            if (i > 0){
                leftProducts[i] = leftProducts[i - 1] * rightProduct;
                rightProduct *= a[i];

            }
            // 待遍历至列表首元素, 其无左边积, 另行处理.
            else{
                leftProducts[i] = rightProduct;
            }
//            System.out.println(leftProducts[i]);
        }
        return leftProducts;
    }
    public static void main(String []args){
        Jianzhi66 s = new Jianzhi66();
        int [] ints = new int[]{1, 2, 3, 4, 5};
        s.constructArr(ints);
    }
}
