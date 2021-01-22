# Uses python3

import sys


def acyclic(adj):
    return 0


import sys


class node:
    def __init__(self, key, adj):
        self.key = key
        self.adj = adj
        self.visited = False
        self.cc = None
        self.present = True


def unexplore(i, li):
    i.visited = False
    for j in i.adj:
        if li[j].visited:
            unexplore(li[j], li)


def explore(i, li):
    i.visited = True
    for j in i.adj:
        if not li[j].visited:
            if explore(li[j], li):
                return True
        else:
            return True
    unexplore(i, li)
    return False


def reach(adj):
    li = []
    for i in range(len(adj)):
        obj = node(i, adj[i])
        li.append(obj)
    for i in li:
        if explore(i, li) is True:
            return True

    return False


print(reach([[1], [2], [0], [0]]))
print(reach([[1, 2, 3], [2], [3, 4], [], []]))
print(reach([[1, 2], [3], [4], [4], []]))
print(reach([[1,4],[],[0,1],[2],[3]]))

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
