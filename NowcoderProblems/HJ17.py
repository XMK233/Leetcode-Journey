'''
https://www.nowcoder.com/practice/119bcca3befb405fbe58abe9c532eb29?tpId=37&tqId=21240&rp=1&ru=%2Fta%2Fhuawei&qru=%2Fta%2Fhuawei%2Fquestion-ranking&tab=answerKey

题目描述
开发一个坐标计算工具， A表示向左移动，D表示向右移动，W表示向上移动，S表示向下移动。从（0,0）点开始移动，从输入字符串里面读取一些坐标，并将最终输入结果输出到输出文件里面。

输入：

合法坐标为A(或者D或者W或者S) + 数字（两位以内）

坐标之间以;分隔。

非法坐标点需要进行丢弃。如AA10;  A1A;  $%$;  YAD; 等。

下面是一个简单的例子 如：

A10;S20;W10;D30;X;A1A;B10A11;;A10;

处理过程：

起点（0,0）

+   A10   =  （-10,0）

+   S20   =  (-10,-20)

+   W10  =  (-10,-10)

+   D30  =  (20,-10)

+   x    =  无效

+   A1A   =  无效

+   B10A11   =  无效

+  一个空 不影响

+   A10  =  (10,-10)

结果 （10， -10）

注意请处理多组输入输出

输入描述:
一行字符串

输出描述:
最终坐标，以逗号分隔

示例1
输入
复制
A10;S20;W10;D30;X;A1A;B10A11;;A10;
输出
复制
10,-10

注意，合法的命令，长度可以是3，也可以是2，比如J20, C9.

'''
ipt = input()
# ipt = "A10;S20;W10;D30;X;A1A;B10A11;;A10;"
commands = ipt.split(";")
directions = {"W": (0, 1), "S": (0, -1), "A": (-1, 0), "D": (1, 0)}
position = (0, 0)
for command in commands:
    if (len(command) == 3\
        and command[0] in "WSAD"\
        and command[1] >= "0" and command[1] <= "9"\
        and command[2] >= "0" and command[2] <= "9") or\
        (len(command) == 2 \
         and command[0] in "WSAD" \
         and command[1] >= "0" and command[1] <= "9")\
        :
        distance = int(command[1:])
        direction = directions[command[0]]
        position = (position[0] + direction[0] * distance, position[1] + direction[1] * distance)
    else:
        continue

print("{},{}".format(position[0], position[1]))
