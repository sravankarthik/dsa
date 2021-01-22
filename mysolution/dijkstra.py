# Uses python3

import sys
import heapq as hp


class node:
    def __init__(self, key, adj, cost):
        self.key = key
        self.adj = adj
        self.cost = cost
        self.distance = sys.maxsize


def distance(adj, cost, s, t):
    li = []
    li_dist = []
    for i in range(len(adj)):
        n = node(i, adj[i], cost[i])
        li.append(n)
        li_dist.append([i, sys.maxsize])
    li_dist[s][1] = 0
    hp.heapify(li_dist)
    j = 1
    while j <= len(li_dist):
        q = hp.nsmallest(j, li_dist, key=lambda x: x[1])
        u = q[j-1][0]
        if u == t and q[j-1][1] != sys.maxsize:
             return q[j-1][1]
        for i in range(len(li[u].adj)):
            if li_dist[li[u].adj[i]][1] > q[j-1][1] + li[u].cost[i]:
                li_dist[li[u].adj[i]][1] = q[j-1][1] + li[u].cost[i]
        j += 1
    if li_dist[t][1] != sys.maxsize:
        return li_dist[t][1]
    return -1


print(distance([[1, 2], [2], [], [0]], [[1, 5], [2], [], [2]], 0, 2))
print(distance([[1, 2], [2], []], [[7, 5], [2], []], 2, 1))
print(distance([[1, 2], [2, 3, 4], [1, 3, 4], [], [3]], [[4, 2], [3, 2, 3], [1, 4, 4], [], [1]], 0, 4))

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
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))
