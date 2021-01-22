# Uses python3
import sys
import math
import heapq


class node:
    def __init__(self, x, y, i):
        self.point = (x, y)
        self.dist = sys.maxsize
        self.num = i


def distance(a, b):
    x1 = a.point[0]
    x2 = b.point[0]
    y1 = a.point[1]
    y2 = b.point[1]
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def minimum_distance(x, y):
    result = 0.
    li = []
    dist_li = []
    for i in range(len(x)):
        e = node(x[i], y[i], i)
        li.append(e)
        dist_li.append([sys.maxsize, i])
    li[0].dist = 0
    dist_li[0][0] = 0
    for i in range(1, len(x) + 1):
        q = min(dist_li, key=lambda x: x[0])
        dist_li.remove(q)
        result += q[0]
        o = li[q[1]]
        for j in dist_li:
            s = distance(o, li[j[1]])
            if s < li[j[1]].dist:
                li[j[1]].dist = s
                j[0] = s

    return result


print(minimum_distance([0, 0, 1, 1], [0, 1, 0, 1]))
print(minimum_distance([0, 0, 1, 3, 3], [0, 2, 1, 0, 2]))


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
