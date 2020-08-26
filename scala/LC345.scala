package main.scala

object LC345 {
  var vowels = List('a', 'e', 'i', 'o', 'u')
  // 判断是不是元音字母
  def isVowel(c: Char): Boolean = {
    return vowels.contains(c)
  }
  // 开始判断
  def reverseVowels(s: String): String = {
    var chars = new Array[Char](s.length)
    for ((i, c) <- 0.until(s.length).zip(s)){
      chars(i) = s(i)
    }
    // 首尾指针
    var head = 0; var tail = s.length - 1
    while(head < tail){
      // 如果是元音字母:
      if ( isVowel(chars(head)) ){
        if (isVowel(chars(tail))){
          // 如果两个都是元音字母, 就互换
          var tmp = chars(head)
          chars(head) = chars(tail)
          chars(tail) = tmp
          head += 1
          tail -= 1
        }
        else{
          tail -= 1
        }
      }
      else{
        head += 1
      }
    }
    return chars.mkString("")
  }
  def main(args: Array[String]): Unit = {
    println(reverseVowels("e"))
    println(reverseVowels("b"))
    println(reverseVowels("ea"))
    println(reverseVowels("ba"))
    println(reverseVowels("ab"))
//    print(this.isVowel('b'))
  }
}
