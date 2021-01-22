import sys


def acyclic(adj):
    return 0


class node:
    def __init__(self, key, adj):
        self.key = key
        self.adj = adj
        self.visited = False
        self.cc = None
        self.present = True


global result
result = []

def check(a, li):
    if a == []:
        return True
    for i in a:
        if li[i] is not None:
            return False
    return True


def explore(i, li):
    global result
    if i is None:
        return
    i.visited = True
    for j in i.adj:
        if li[j] is not None and not li[j].visited:
            explore(li[j], li)
    if check(i.adj, li):
        result.append(i.key)
        li[li.index(i)] = None
        return



def reach(adj):
    li = []
    for i in range(len(adj)):
        obj = node(i, adj[i])
        li.append(obj)
    for i in li:
        explore(i, li)
    print(result)


#print(reach([[1, 2], [3], [4], [4], []]))
print(reach([[1, 2], [], [1], [2], [0, 3]]))

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
