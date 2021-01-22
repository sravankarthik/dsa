# Uses python3

import sys
import queue


class node:
    def __init__(self, key, adj):
        self.key = key
        self.adj = adj
        self.dist = -1


def distance(adj, s, t):
    if s == t:
        return 0
    li = []
    for i in range(len(adj)):
        obj = node(i, adj[i])
        li.append(obj)
    k = [li[s]]
    li[s].dist = 0
    while k:
        u = k.pop(0)
        for j in u.adj:
            if li[j].key == t:
                return u.dist + 1
            if li[j].dist == -1:
                k.append(li[j])
                li[j].dist = u.dist + 1
    return -1


print(distance([[1, 2, 3], [0, 2], [0, 1], [0]], 1, 3))
print(distance([[2, 3], [4], [0, 2], [0, 2], [1]], 2, 4))

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t))
