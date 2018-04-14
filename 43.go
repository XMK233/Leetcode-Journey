package main

import (
	"fmt"
	"strconv"
)
/*
num1与num2的乘积的位数为两个数位数之和（实际位数不一定这么长）
num1第i位的数字乘上num2第j位的数字得到的结果一定是一个两位数。
这个两位数的高位会位于乘积的第(i + j)位，低位会位于乘积的第(i + j + 1)位。

然后遍历乘积数组，将每一个数的个位留在本位置，其他位的数字作为进位。
这一步作为修正步，将乘积数组修正为正常的数字形式。
再将乘积数组变成字符串形式，利用的是strconv.Itoa()方法。
* */
func multiply(num1 string, num2 string) string {
	var sum []int = make([]int, len(num1) + len(num2))
	i := len(num2) - 1
	for ; i >= 0; i--{
		j := len(num1) - 1
		for ;j >= 0; j--{
			m := (num2[i] - 48) * (num1[j] - 48)
			mH := int(m / 10)
			mL := int(m % 10)
			sum[i + j] += mH
			sum[i + j + 1] += mL
		}
	}
	var o int = 0
	for  k := len(sum) - 1; k >= 0; k--{
		tmp := sum[k] + o
		mH := int(tmp / 10)
		mL := int(tmp % 10)
		sum[k] = mL
		o = mH
	}

	var str string = ""
	flag := 0
	for k := 0; k < len(sum); k++{
		if sum[k] != 0 && flag == 0{
			flag = 1
		}
		if flag == 1{
			str += strconv.Itoa(sum[k])
		}
	}
	if len(str) == 0{
		str = "0"
	}
	return str
}
func main() {
	//var a  = []int{0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1}
	var s1, s2 string
	s1 = "3"
	s2 = "2"
	fmt.Println(multiply(s1, s2))
}