l = [1, 2, 3, 4, 5, 5, 9]
def binarySearch(l, target):
    head, tail = 0, len(l) - 1
    while tail >= head: ##
        mid = head + (tail - head) // 2
        if l[mid] >= target:
            tail = mid - 1
        else:
            head = mid + 1
    print(head)
print(binarySearch(l, 5))