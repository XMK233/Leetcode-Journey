public class Jianzhi51 {
    private int reverseOrder = 0;
    public int[] mergeSort(int[]nums){
        // 如果数组较短，可以直接处理。
        if (nums.length <= 1){
            return nums;
        }
        // 数组较长，就得麻烦点。
        // 先分割数组
        int mid = nums.length / 2 - 1;
        int []leftList = new int [mid - 0 + 1];
        int []rightList = new int [(nums.length - 1) - (mid + 1) + 1];
        for (int i = 0; i < nums.length; i++){
            if (i <= mid){
                leftList[i] = nums[i];
            }
            else{
                rightList[i-mid-1] = nums[i];
            }
        }
        // 分别排序
        leftList = mergeSort(leftList);
        rightList = mergeSort(rightList);
        int []resSorted = new int[nums.length];
        // 然后就可以合并了。
        int leftIndex = 0, rightIndex = 0, resIndex = 0;
        while (leftIndex < leftList.length && rightIndex < rightList.length){
            // 如果左边的头一个数字比右边的头一个数字大， 那么左边剩余的所有数字都比右边头一个数字大
            // 所以左边的数字和右边头一个数字的组合全都是逆序对。
            if (leftList[leftIndex] > rightList[rightIndex]){
                reverseOrder += leftList.length - leftIndex;
                resSorted[resIndex] = rightList[rightIndex];
                rightIndex++;
                resIndex++;
            }
            else{
                resSorted[resIndex] = leftList[leftIndex];
                leftIndex++;
                resIndex++;
            }
        }
        while (leftIndex < leftList.length){
            resSorted[resIndex] = leftList[leftIndex];
            leftIndex++;
            resIndex++;
        }
        while (rightIndex < rightList.length){
            resSorted[resIndex] = rightList[rightIndex];
            rightIndex++;
            resIndex++;
        }
        return resSorted;
    }
    public int reversePairs(int[] nums) {
        // 特殊情况：数组的长度较小
        if (nums.length <= 1)
            return 0;
        // 如果数组的长度较大
        mergeSort(nums);
        return reverseOrder;

    }
    public static void main(String []args){
        Jianzhi51 s = new Jianzhi51();
        int [] res = new int[]{7, 5, 6, 4};
//        s.mergeSort(res);
        System.out.print(s.reversePairs(res));
    }
}

