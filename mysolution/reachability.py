#Uses python3

import sys


class node:
    def __init__(self, key, adj):
        self.key = key
        self.adj = adj
        self.visited = False
        self.cc = None


def explore(i, li, y):
    count = 0
    if y == i:
        return True
    i.visited = True
    for j in i.adj:
        if not li[j].visited:
            if explore(li[j], li, y) is True:
                count = 1
    if count == 1:
        return True
    else:
        return False


def reach(adj, x, y):
    li = []
    for i in range(len(adj)):
        obj = node(i, adj[i])
        li.append(obj)
    return explore(li[x], li, li[y])


print(reach([[1,3],[0,2],[1,3],[0,2]],0,3))
print(reach([[1],[2],[1],[]],0,3))

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[2 * m:]
    adj = [[] for _ in range(n)]
    x, y = x - 1, y - 1
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(reach(adj, x, y))
