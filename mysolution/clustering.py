# Uses python3
import sys
import math


def distance(a, b):
    x1 = a.point[0]
    x2 = b.point[0]
    y1 = a.point[1]
    y2 = b.point[1]
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


class node:
    def __init__(self, x, y, i, o):
        self.point = (x, y)
        self.index = i
        self.parent = i
        self.dist = o


def find(i, parent):
    if i != parent[i]:
        parent[i] = find(parent[i], parent)
    return parent[i]


def union(x, y, parent):
    parent[y] = find(parent[x], parent)
    return

def check(li, k):
    res = []
    count = 0
    for i in li:
        if i not in res:
            res.append(i)
            count += 1
    if count == k:
        return True



def clustering(x, y, k):
    li = []
    li_dist = []
    o = [None for _ in range(len(x))]
    for i in range(len(x)):
        j = node(x[i], y[i], i, o)
        li.append(j)
    for i in range(len(li) - 1):
        a = li[i]
        for j in range(i + 1, len(li)):
            b = li[j]
            c = distance(a, b)
            li_dist.append([c, a, b, i, j])
            li[i].dist[j] = c
            li[j].dist[i] = c
    li_dist.sort(key=lambda x: x[0])
    parent = [i for i in range(len(x))]
    for i in range(len(li_dist)):
        if find(li_dist[i][3], parent) != find(li_dist[i][4], parent):
            union(li_dist[i][3], li_dist[i][4], parent)
            for j in range(len(parent)):
                find(j, parent)
        if find(li_dist[i+1][3], parent) != find(li_dist[i+1][4], parent) and check(parent, k):
            return li_dist[i+1][0]



    return -1.


print(clustering([7, 4, 5, 1, 2, 5, 3, 7, 2, 4, 6, 2], [6, 3, 1, 7, 7, 7, 3, 8, 8, 4, 7, 6], 3))
print(clustering([3, 1, 4, 9, 9, 8, 3, 4], [1, 2, 6, 8, 9, 9, 11, 12], 4))

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    data = data[1:]
    x = data[0:2 * n:2]
    y = data[1:2 * n:2]
    data = data[2 * n:]
    k = data[0]
    print("{0:.9f}".format(clustering(x, y, k)))
