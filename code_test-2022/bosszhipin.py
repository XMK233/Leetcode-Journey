l = [1, 5, 6, 7, 2]

def merge_sort(l):
    if len(l) <= 1:
        return l
    mid_point = len(l) // 2
    left_part = merge_sort(l[0:mid_point])
    right_part = merge_sort(l[mid_point:])

    # for left_val in left_part[::-1]:
    #     for right_val in right_part:
    #         if left_val > right_val:
    #             print(f'({left_val},{right_val})')
    #         else:
    #             break

    tmp = []
    i, j = 0, 0
    while i < len(left_part) and j < len(right_part):  ## TODO
        if left_part[i] < right_part[j]:
            tmp.append(left_part[i])
            i += 1
        else:
            tmp.append(right_part[j])
            print(f'({left_part[i]},{right_part[j]})')
            j += 1
    if i == len(left_part):
        tmp.extend(right_part[j:])
    else:
        tmp.extend(left_part[i:])
    return tmp

# def output_reverse_tuple(l):
#     if len(l) <= 1:
#         return
#
#     mid_point = len(l)//2
#
#     output_reverse_tuple(l[0:mid_point])
#     output_reverse_tuple(l[mid_point:])

    # tmp_left = sorted(l[0:mid_point])
    # tmp_right = sorted(l[mid_point:])
    #
    # # for i in range(len(tmp_left), -1, -1):
    # for left_val in tmp_left[::-1]:
    #     for right_val in tmp_right:
    #         if left_val > right_val:
    #             print(f'({left_val},{right_val})')
    #         else:
    #             break


merge_sort(l)