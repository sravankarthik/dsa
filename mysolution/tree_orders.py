# python3

import sys
import threading

sys.setrecursionlimit(10 ** 6)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size


class node:
    def __init__(self, value=None):
        self.key = value
        self.parent = None
        self.right_child = None
        self.left_child = None


class binary_search_tree:
    def __init__(self, values, lefts, rights):
        self.root = None
        self.values = values
        self.lefts = lefts
        self.rights = rights
        self.insert()

    def insert(self):
        if self.root is None:
            self.root = node(self.values[0])
            # self.root.left_child = node(self.values[self.lefts[0]])
            # self.root.right_child = node(self.values[self.rights[0]])
            self.insert_(self.root, self.lefts[0], self.rights[0])
            # self.insert_(self.root.right_child, self.lefts[0], self.rights[0])

    def insert_(self, n, l, r):
        if l != -1:
            a = node(self.values[l])
            n.left_child = a
            n.left_child.parent = n
            self.insert_(n.left_child, self.lefts[l], self.rights[l])

        if r != -1:
            a = node(self.values[r])
            n.right_child = a
            n.right_child.parent = n
            self.insert_(n.right_child, self.lefts[r], self.rights[r])


# x = binary_search_tree([4, 2, 5, 1, 3], [1, 3, -1, -1, -1], [2, 4, -1, -1, -1])
# = binary_search_tree([0, 10, 20, 30, 40, 50, 60, 70, 80, 90], [7, -1, -1, 8, 3, -1, 1, 5, -1, -1],
# [2, -1, 6, 9, -1, -1, -1, 4, -1, -1])

class TreeOrders:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        for i in range(self.n):
            [a, b, c] = map(int, sys.stdin.readline().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c
        self.tree = binary_search_tree(self.key, self.left, self.right).root


    def inOrder(self):
        self.result = []
        # Finish the implementation
        # You may need to add a new recursive method to do that
        self.inorder(self.tree)

        return self.result

    def inorder(self, t):
        if t is None:
            return
        self.inorder(t.left_child)
        print(t.key, end=" ")
        self.inorder(t.right_child)


    def preOrder(self):
        self.result = []
        # Finish the implementation
        # You may need to add a new recursive method to do that
        self.preorder(self.tree)

        return self.result

    def preorder(self, t):
        if t is None:
            return
        print(t.key, end=" ")
        self.preorder(t.left_child)
        self.preorder(t.right_child)

    def postOrder(self):
        self.result = []
        # Finish the implementation
        # You may need to add a new recursive method to do that
        self.postorder(self.tree)

        return self.result

    def postorder(self, t):
        if t is None:
            return
        self.postorder(t.left_child)
        self.postorder(t.right_child)
        print(t.key, end=" ")


def main():
    tree = TreeOrders()
    tree.read()
    tree.inOrder()
    print()
    tree.preOrder()
    print()
    tree.postOrder()


threading.Thread(target=main).start()
