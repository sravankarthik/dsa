# python3
import math


class heap:
    def __init__(self, data):
        self.data = data
        self.swap = []
        self.size = len(data)

    def parent(self, i):
        return math.floor((i - 1) / 2)

    def leftchild(self, i):
        return 2 * i + 1

    def rightchild(self, i):
        return 2 * i + 2

    def siftup(self, i):
        while i > 0 and self.data[self.parent(i)] < self.data[i]:
            self.data[self.parent(i)], self.data[i] = self.data[i], self.data[self.parent(i)]
            i = self.parent(i)

    def siftdown(self, i):
        max_index = i
        left = self.leftchild(i)
        if left < self.size and self.data[max_index] > self.data[left]:
            max_index = left
        right = self.rightchild(i)
        if right < self.size and self.data[max_index] > self.data[right]:
            max_index = right
        if i != max_index:
            self.swap.append((i, max_index))
            self.data[max_index], self.data[i] = self.data[i], self.data[max_index]
            self.siftdown(max_index)

    def insert(self, p):
        self.data.append(p)

        self.siftup(self.size)

        self.size += 1

    def heapsort(self):
        self.swap = []
        self.size -= 1
        for i in range(self.size):
            print(self.swap)
            self.data[0], self.data[self.size] = self.data[self.size], self.data[0]
            self.size -= 1
            self.siftdown(0)

    def buildheap(self):
        n = self.size

        for i in range(math.floor((n-1)/2), -1, -1):

            self.siftdown(i)




def build_heap(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    # The following naive implementation just sorts the given sequence
    # using selection sort algorithm and saves the resulting sequence
    # of swaps. This turns the given array into a heap, but in the worst
    # case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    x = heap(data)
    x.buildheap()
    return x.swap


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
