package main.scala
import scala.collection.mutable
//import scala.collection.mutable.Map
import scala.collection.mutable.ArrayBuffer

object LC350 {
  def processDict(m: mutable.Map[Int, Int], num: Int): mutable.Map[Int, Int] = {
    /*
    * 如果num是key, 那么相应value减一; 如果减到0, 就删掉这个key.
    * */
    if (m.contains(num)){
      var storage = m(num) - 1
      if (storage == 0){
        m.remove(num)
      }
      else{
        m += (num -> storage)
      }
    }
    return m
  }
  //
  def toDict(a: Array[Int]): mutable.Map[Int, Int] = {
    /*
    * 转为dict. key为字符, value为出现次数.
    * */
    var m : mutable.Map[Int, Int] = mutable.Map()
    for (c <- a){
      if (m.contains(c)){
        m(c) += 1
      }
      else{
        m += (c -> 1)
      }
    }
    return m
  }
  //
  def intersect(nums1: Array[Int], nums2: Array[Int]): Array[Int] = {
    // 变长数组: scala.collection.mutable.ArrayBuffer
    var ab: ArrayBuffer[Int] = new ArrayBuffer[Int]()
    // 将两个数组化为dict
    var dict1 = this.toDict(nums1)
    var dict2 = this.toDict(nums2)
    //找更短的数组.
    var shorterOne: Array[Int] = if (nums1.length < nums2.length) nums1 else nums2
    // 遍历更短的数组
    for (n <- shorterOne){
      if (dict1.contains(n) && dict2.contains(n)){
        ab += n
        dict1 = this.processDict(dict1, n)
        dict2 = this.processDict(dict2, n)
      }
    }
//    print(ab.toString)
    return ab.toArray
  }
  def main(args: Array[String]): Unit = {
    // this.toDict(Array(1, 2, 3, 3, 3))
    this.intersect(Array(4,9,5), Array(9,4,9,8,4))

  }
}
