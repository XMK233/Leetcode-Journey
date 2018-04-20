package main

import (
	"fmt"
)
/*
matrix[k + i][n - 1 + k]存到matrix[k + i][n - 1 + k]
matrix[k + i][n - 1 + k]存到matrix[n - 1 + k][n - 1 + k - i]
matrix[n - 1 + k][n - 1 + k - i]存到matrix[n - 1 - i + k][k]
matrix[n - 1 - i + k][k]存到matrix[k][k + i]
上述公式首先得推出来。
然后就是考虑一些什么终止条件啊之类的。
上述方法是按部就班地作旋转，非常直观的解决方案。自己推很轻松，但是事后回来看可能不好看懂。

其实最好的方法是这样的：以中间的行为轴，将行放到对称位置；之后以主对角线为轴作转置即可。
不过这种方法的原理，网上没人解释。难道说这就是一个纯粹的技巧题？
* */
func rotate(matrix [][]int)  {
	var n int = len(matrix)//数组的维数
	var k int = 0//层数。一开始是从[0][0]开始遍历，后来就是从[1][1]开始，这就是层
	for ;n > 0;{
		var i int = 0
		for ; i < n - 1; i++{
			tmp := matrix[k + i][n - 1 + k]
			matrix[k + i][n - 1 + k] = matrix[k][k + i]
			tmp1 := matrix[n - 1 + k][n - 1 + k - i]
			matrix[n - 1 + k][n - 1 + k - i] = tmp
			tmp2 := matrix[n - 1 - i + k][k]
			matrix[n - 1 - i + k][k] = tmp1
			matrix[k][k + i] = tmp2
		}
		n -= 2
		k++
	}
}
func main() {
	//var a  = []int{1, 2}
	var b = [][]int {{1,2,3}, {4,5,6}, {7,8,9}}
	rotate(b)
	fmt.Println(b)
}