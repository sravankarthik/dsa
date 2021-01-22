# Uses python3

import sys


class node:
    def __init__(self, key, adj):
        self.key = key
        self.adj = adj
        self.visited = False
        self.cc = None


def explore(i, li):
    i.visited = True
    for j in i.adj:
        if not li[j].visited:
            explore(li[j], li)


def number_of_components(adj):
    li = []
    for i in range(len(adj)):
        obj = node(i, adj[i])
        li.append(obj)
    count = 0
    for i in li:
        if not i.visited:
            explore(i, li)
            count += 1

    return count

print(number_of_components([[1],[2],[1],[]]))

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
    print(number_of_components(adj))
