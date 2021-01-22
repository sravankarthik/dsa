# Uses python3

import sys
import queue


class node:
    def __init__(self, key, adj):
        self.key = key
        self.adj = adj
        self.c = None


def bipartite(adj):
    li = []
    for i in range(len(adj)):
        obj = node(i, adj[i])
        li.append(obj)
    k = [li[0]]
    li[0].c = 'r'
    while k:
        u = k.pop(0)
        for j in u.adj:
            if li[j].c is None:
                if u.c == 'r':
                    k.append(li[j])
                    li[j].c = 'b'
                    continue
                elif u.c == 'b':
                    k.append(li[j])
                    li[j].c = 'r'
                    continue
            elif li[j].c == 'r' and u.c == 'r':
                return 0
            elif li[j].c == 'b' and u.c == 'b':
                return 0
    return 1


print(bipartite([[3], [3, 4], [3], [0, 1, 2], [1]]))
print(bipartite([[1, 2, 3], [0, 2], [0, 1], [0]]))

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
    print(bipartite(adj))
