package main
import "fmt"

func firstMissingPositive(nums []int) int {
	//如果数组里面什么元素都没有，那自然就是返回1
	if len(nums) == 0{
		return 1
	}

	//如果数组里面有一些元素，那么就展开判断
	//思路的核心是什么呢？
	//遍历数字，把nums[i]位置的正数tmp和nums[tmp - 1]的位置处的数字置换一下。
	//这里注意一下，如果不是正数，什么都不用做；如果发现数组不够长，没有nums[tmp-1]位置，也什么都别做。
	//如果能够置换，看看原nums[tmp-1]位置的元素是不是正数，若是的话，下次遍历从这里开始；若非，就正常地接下去遍历。
	for i := 0; i < len(nums); i++{
		tmp := nums[i]
		if tmp > 0{//nums[i]为正数
			if tmp <= len(nums) && nums[tmp - 1] != tmp{//能放在nums[tmp - 1]处
				t := nums[tmp - 1]
				nums[tmp - 1] = tmp
				nums[i] = t
				if nums[i] > 0{//如果交换过来的数字是正数，那么就接着调整这个数字的位置。
					i--
				}
			}
		}
	}

	//相信所有的nums[i]都被放到预计位置了。
	//再次遍历数组，发现nums[i]上的数字不是i + 1
	//那么i + 1就是缺失的正数
	for i := 0; i < len(nums); i++{
		if nums[i] != i + 1{
			return i + 1
		}
	}

	//默认返回值：如果没有缺失的正数，比如数组是{1， 2， 3， 4， 5}，那么就默认返回6，也就是
	//len(nums) + 1，数组中没有出现、却又即将出现的正数。
	return len(nums) + 1
}
func main() {
	/* 这是我的第一个简单的程序 */
	//fmt.Println("Hello, World!")
	var a  = []int{3, 4, -1, 1}
	fmt.Println(firstMissingPositive(a))
}