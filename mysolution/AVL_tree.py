class node:
    def __init__(self, value=None):
        self.key = value
        self.parent = None
        self.right_child = None
        self.left_child = None
        self.height = 1


class AVL_tree:
    def __init__(self):
        self.root = None

    def adjust_height(self, n):
        n.height = 1 + max(n.left.height, n.right.height)

    def avl_insert(self, k, r=None):
        if r is None:
            r = self.root
        self.insert(k, r)
        n = self.find(k, r)
        self.rebalance(n)

    def rebalance(self, n):
        p = n.parent
        if n.left_child.height > n.right_child.height + 1:
            self.rebalance_right(n)
        elif n.right_child.height > n.left_child + 1:
            self.rebalance_left(n)
        self.adjust_height(n)
        if p is not None:
            self.rebalance(p)

    def rebalance_right(self, n):
        m = n.left_child
        if m.right_child.height > m.left.height:
            self.rotate_right(m)
        self.rotate_right(n)

    def rebalance_left(self, n):
        m = n.right_child
        if m.left_child.height > m.right.height:
            self.rotate_left(m)
        self.rotate_left(n)

    def find(self, x, r):
        if x == r.key:
            return r
        elif x > r.key:
            if r.right_child is None:
                return r
            else:
                return self.find(x, r.right_child)
        elif x < r.key:
            if r.left_child is None:
                return r
            else:
                return self.find(x, r.left_child)

    def insert(self, value, r=None):
        if self.root is None:
            self.root = node(value)
        else:
            p = self.find(value, self.root)
            if value > p.key:
                p.right_child = node(value)
                p.right_child.parent = p
                p.right_child.height = 1 + p.height
            elif value < p.key:
                p.left_child = node(value)
                p.left_child.parent = p
                p.left_child.height = 1 + p.height
            if p.key == value:
                print("Already in tree")

    def print_(self):
        if self.root is None:
            print("tree empty")
        else:
            self._print(self.root)

    def _print(self, r):
        if r is not None:
            self._print(r.left_child)
            print(r.key)
            self._print(r.right_child)

    def height(self):
        if self.root is None:
            return 0
        else:
            return self._height(self.root)

    def _height(self, r):
        if r is None:
            return 0
        return 1 + max(self._height(r.left_child), self._height(r.right_child))

    def next(self, i):
        n = self.find(i, self.root)
        if n.right_child is not None:
            return self.left_des(n.right_child)
        else:
            return self.right_ans(n)

    def left_des(self, n):
        if n.left_child is None:
            return n
        else:
            return self.left_des(n.left_child)

    def right_ans(self, n):
        if n.parent is None:
            return n
        if n.parent.key > n.key:
            return n.parent
        else:
            self.right_ans(n.parent)

    def range_search(self, a, b):
        l = []
        n = self.find(a, self.root)
        while n.key < b:
            if n.key > a:
                l.append(n.key)
            n = self.next(n.key)
        return l

    def delete(self, n):
        a = self.find(n, self.root)
        if a.right_child is None and a.left_child is None:
            if a == a.parent.left_child:
                a.parent.left_child = None
            else:
                a.parent.right_child = None
            return

        elif a.right_child is None and a.parent is not None:
            if a == a.parent.left_child:
                a.parent.left_child = a.left_child
                a.left_child.parent = a.parent
            else:
                a.parent.right_child = a.left_child
                a.left_child.parent = a.parent
            return
        elif a.left_child is None and a.parent is not None:
            if a == a.parent.left_child:
                a.parent.left_child = a.right_child
                a.right_child.parent = a.parent
            else:
                a.parent.right_child = a.right_child
                a.right_child.parent = a.parent
            return
        x = self.next(n)
        u = x.key
        self.delete(x.key)
        a.key = u
        return