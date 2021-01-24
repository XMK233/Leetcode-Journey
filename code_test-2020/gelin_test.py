def calc_inters(bbox1, bbox2):
    return min(bbox1[2], bbox2[2]) - max(bbox1[0], bbox2[0]) > 0 and min(bbox1[3], bbox2[3]) - max(bbox1[1], bbox2[1]) > 0

def calc_count(anchors, dets, k):
    count = 0
    for jj in range(len(anchors.keys())):
        for ii in range(k):
            if calc_inters(anchors[jj], dets[ii]):
                count += 1
                break
    return count

def gen_anchors(w, h, s, t, P, Q):
    anchors = {}
    si = 0
    kk = 0
    while si + w <= P:
        tj = 0
        while tj + h <= Q:
            anchors[kk] = [si, tj, si + w, tj + h]
            kk += 1
            tj += t
        si += s
    return anchors

def get_inputs():
    # input
    w, h, s, t, k, P, Q = 2, 3, 3, 2, 1, 11, 15 # list(map(int, input().strip().split()))
    # dets
    dets = {}
    for ii in range(k):
        X, Y, W, H = list(map(int, input().strip().split()))
        dets[ii] = [X, Y, X + W, Y + H]
    return w, h, s, t, P, Q, dets, k

#anchors
w, h, s, t, P, Q, dets, k = get_inputs()
anchors = gen_anchors(w, h, s, t, P, Q)

# calc
print(calc_count(anchors, dets, k))