import sys
import threading


class treeheight:
    def __init__(self, li, n):
        self.parent = li
        self.n = n
        self.cache = [0]*n

    def height(self, i):
        if self.parent[i] == -1:
            return 1
        else:
            if self.cache[i]!=0:
                return self.cache[i]
            else:
                self.cache[i] = 1 + self.height(self.parent[i])
            return self.cache[i]
def main():
    n = int(input())
    li = list(map(int, sys.stdin.readline().split()))
    root = treeheight(li,n)
    s=[]
    for i in range(n):
        s.append(root.height(i))
    print(max(s))
sys.setrecursionlimit(10 ** 7)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size
threading.Thread(target=main).start()