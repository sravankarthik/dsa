import sys


class node:
    def __init__(self, key, adj, cost):
        self.key = key
        self.adj = adj
        self.cost = cost
        self.distance = sys.maxsize


def negative_cycle(adj, cost):
    li = []
    for i in range(len(adj)):
        n = node(i, adj[i], cost[i])
        li.append(n)
    li[0].distance = 0
    for _ in range(len(adj) - 1):
        for i in range(len(li)):
            for j in range(len(li[i].adj)):
                if li[li[i].adj[j]].distance > li[i].distance + li[i].cost[j]:
                    li[li[i].adj[j]].distance = li[i].distance + li[i].cost[j]
    for i in range(len(li)):
        for j in range(len(li[i].adj)):
            if li[li[i].adj[j]].distance > li[i].distance + li[i].cost[j]:
                return 1
    return 0


print(negative_cycle([[1], [2], [0], [0]], [[-5], [2], [1], [2]]))
print(negative_cycle([[1, 2], [2], [3, 4], [1, 4], []], [[4, 3], [-2], [-3, 1], [4, 2], []]))
print(negative_cycle([[1, 2], [2, 3], [3, 4], [4], []], [[4, 3], [-2, 4], [-3, 1], [2], []]))


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    print(negative_cycle(adj, cost))
