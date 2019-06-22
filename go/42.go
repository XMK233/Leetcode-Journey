/*
* 找左右边界的当中更小的那个作为最小值。
* 左右边界哪边更小，哪边就往另一头移动。
* 只有边界的中间存在比最小值还小的值，才能够蓄水。
* 如果发现找到了比最小值更大的值，那么就得重新寻找最小值了。
* 如果形成了蓄水条件，那么最小值就是水位的上限。
* 左右边界碰在一起就结束了。
* */
func trap(height []int) int {
	res, left := 0, 0
	right := len(height) - 1

	for left < right{
		//minh :=  height[left] < height[right] ? height[left] : height[right]

		if height[left] <= height[right]{
			minh := height[left]
			left++
			for left < right && height[left] < minh{
				res = res + minh - height[left]
				left++
			}
		}else{
			minh := height[right]
			right--
			for right > left && height[right] < minh{
				res = res + minh - height[right]
				right--
			}
		}
	}
	return res
}
func main() {
	var a  = []int{0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1}
	fmt.Println(trap(a))
}