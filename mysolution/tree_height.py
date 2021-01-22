# python3

import sys
import threading

def h(li):
    dicty = {}
    for i in li:
        if i in dicty.keys():
            dicty[i] += 1
        else:
            dicty[i] = 1
    return len(dicty.keys())



def compute_height(n, parents):
    # Replace this code with a faster implementation
    max_height = 0
    for vertex in range(n):
        height = 0
        current = vertex
        while current != -1:
            height += 1
            current = parents[current]
        max_height = max(max_height, height)
    return max_height


class Treenode:
    def __init__(self, data, children=None, parent=None):
        if children is None:
            children = []
        self.data = data
        self.children = children
        self.parent = parent

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def height(self):
        level = 0
        itr = self.parent
        while itr:
            level += 1
            itr = itr.parent
        return level

    def print_(self):
        print(self.data)
        if self.children:
            for i in self.children:
                i.print_()
'''root = Treenode(1)
root.add_child(Treenode(2))
k = Treenode(3)
root.add_child(k)
s = Treenode(4)
k.add_child(s)
print(s.height())
root.print_()'''


def main():
    dicty = {0:0}
    i=0
    root = None
    n = int(input())
    li = list(map(int, input().split()))
    #print(h(li))

    for i in range(len(li)):
        if li[i] == -1:
            root = Treenode(i)
            break

    def tree(x, root, li):
        for i in range(len(li)):
            if li[i] == x:
                s = Treenode(i)
                root.add_child(s)
                dicty[0]=max(s.height(),dicty[0])
                tree(i, s, li)
        return dicty[0]+1
    print(tree(i,root,li))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10 ** 7)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size
threading.Thread(target=main).start()
