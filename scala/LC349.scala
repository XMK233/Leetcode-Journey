package main.scala
import scala.collection.mutable.Map

object LC349 {
  def intersection(nums1: Array[Int], nums2: Array[Int]): Array[Int] = {
    // 道理上来讲非常简单, 就是利用一些已经实现好了的方法就行了.
    // 在scala里面, 蛮多什么toArray, toSet之类的玩意儿. 用好就行.
    var set_nums1 = nums1.toSet
    var set_nums2 = nums2.toSet
    return set_nums1.&(set_nums2).toArray

    return Array(1, 2, 3)
  }
  def main(args: Array[String]): Unit = {
    print(
      this.intersection(
        Array(4,9,5),
        Array(9,4,9,8,4)
      ).toList
    )
  }
}
