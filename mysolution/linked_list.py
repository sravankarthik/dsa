class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Linkedlist:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def print_(self):
        itr = self.head
        while itr:
            print(itr.data, end=' ')
            itr = itr.next
        print()
        return

    def push_front(self, data):
        node = Node(data)
        if self.head is None and self.tail is None:
            self.head = node
            self.tail = node
            return
        node.next = self.head
        self.head = node

    def push_back(self, data):
        node = Node(data)
        if self.head is None and self.tail is None:
            self.head = node
            self.tail = node
            return
        self.tail.next = node
        self.tail = node

    def top_front(self):
        return self.head.data

    def top_back(self):
        return self.tail.data

    def empty(self):
        if self.head is None:
            return True
        return False

    def pop_front(self):
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return
        x = self.head.data
        self.head = self.head.next
        return x

    def pop_back(self):
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return
        itr = self.head
        while itr.next is not self.tail:
            itr = itr.next
        x = itr.next.data
        self.tail = itr
        itr.next = None
        return x

    def find(self, data):
        itr = self.head
        while itr:
            if itr.data == data:
                return True
            itr = itr.next
        return False

    def erase(self, data):
        if data == self.head.data:
            x = self.pop_front()
            return
        if data == self.tail.data:
            x = self.pop_back()
            return
        itr = self.head
        while itr:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next

    def add_before(self, data, n):
        if n == self.head.data:
            self.push_front(data)
            return
        node = Node(data)
        itr = self.head
        while itr:

            if itr.next.data == n:
                node.next = itr.next
                itr.next = node
                return
            itr = itr.next

    def add_after(self, data, n):
        if n == self.tail.data:
            self.push_back(data)
            return
        node = Node(data)

        itr = self.head
        if n == self.head.data:
            node.next = itr.next
            itr.next = node
            return
        while itr:
            if itr.next.data == n:
                node.next = itr.next.next
                itr.next.next = node
                return
            itr = itr.next


ll = Linkedlist()
ll.push_front(5)
ll.push_front(10)
ll.push_front(15)
ll.print_()
print(ll.top_front())
print(ll.top_back())
print(ll.empty())
print(ll.pop_back())
ll.push_back(5)
print(ll.find(5))
ll.erase(10)
ll.print_()
ll.push_front(3)
ll.add_before(10, 15)
ll.print_()
