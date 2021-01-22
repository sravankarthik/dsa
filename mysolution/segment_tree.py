import math
import sys

# k = int(input())
# arr = []
# for i in range(k):
#    arr.append(int(input()))
arr = [1,3,5,7,9,11]
k = 6
g = math.ceil(math.log(k, 2))
li = [sys.maxsize] * int((2 ** (g+1) - 1))


def segment(arr, li, l, r, p):
    if l == r:
        li[p] = arr[l]
        return
    mid = int((l + r) / 2)
    segment(arr, li, l, mid, 2 * p + 1)
    segment(arr, li, mid + 1, r, 2 * p + 2)
    li[p] = min(li[2 * p + 1], li[2 * p + 2])
    return

segment(arr, li, 0, 5, 0)
print(li)