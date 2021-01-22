class node:
    def __init__(self, value=None):
        self.key = value
        self.parent = None
        self.right_child = None
        self.left_child = None
        # self.height = None


class binary_search_tree:
    def __init__(self):
        self.root = None

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
            elif value < p.key:
                p.left_child = node(value)
                p.left_child.parent = p
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


tree = binary_search_tree()
tree.insert(1)
tree.insert(3)
tree.insert(5)
tree.delete(1)

tree.insert(7)
tree.insert(9)
tree.insert(4)
tree.insert(2)
tree.insert(6)
tree.insert(8)
tree.delete(4)
tree.delete(2)
tree.delete(3)
tree.delete(5)
tree.delete(7)
tree.print_()

# print(tree.height())
# print(tree.next(7).key)
# print(tree.range_search(1, 7))
