'''
要点有几个:
1. 如何判断两个框重叠?
2. 如何遍历所有的先验框?
3. 如何优化算法?

'''

# def calc_count(anchors, dets, k):
#     count = 0
#     for jj in range(len(anchors.keys())):
#         for ii in range(k):
#             if intersectOrNot(anchors[jj], dets[ii]):
#                 count += 1
#                 break
#     return count
#
# def gen_anchors(w, h, s, t, P, Q):
#     anchors = {}
#     si = 0
#     kk = 0
#     while si + w <= P:
#         tj = 0
#         while tj + h <= Q:
#             anchors[kk] = [si, tj, si + w, tj + h]
#             kk += 1
#             tj += t
#         si += s
#     return anchors

#anchors
#######################################33
w, h, s, t, k, P, Q = [int(j) for j in input().split()] # 2, 3, 3, 2, 1, 11, 15
tarBox = []
for i in range(k):
    X, Y, W, H = [int(j) for j in input().split()]
    tarBox.append([X, Y, X + W, Y + H])

################################################
# w, h, s, t, k, P, Q = 1, 1, 1, 1, 1, 13, 10
# X, Y, W, H = 9, 4, 1, 1
# # X, Y, W, H = 4, 7, 17, 13 ## 这里是输入, 到时候改成input类型的.
# tarBox = []
# tarBox.append([X, Y, X + W, Y + H])
##################################################################################################
counter = 0
for n in range(k):
    x = 0
    while x + w <= P:
        if x + w < tarBox[n][0] or x > tarBox[n][2]:
            ## 剪枝策略: 如果在横轴上已不可能与目标框有任何交集.
            pass
        else:
            y = 0
            while y + h <= Q:
                newBox = [x, y, x + w, y + h]
                haveIntersec = min(newBox[3], tarBox[n][3]) > max(newBox[1], tarBox[n][1]) and min(newBox[2], tarBox[n][2]) > max(newBox[0], tarBox[n][0])
                if haveIntersec:
                    counter += 1
                y += t
        x += s

print(counter)

# calc
# print(calc_count(anchors, dets, k))