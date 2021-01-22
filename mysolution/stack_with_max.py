#python3
import sys


class StackWithMax():
    def __init__(self):
        self.__stack = []
        self.maxx = []

    def Push(self, a):
        self.__stack.append(a)
        if len(self.maxx)==0:
            self.maxx.append(a)
        if a>self.maxx[-1]:
            self.maxx.append(a)
        else:
            self.maxx.append(self.maxx[-1])


    def Pop(self):
        assert(len(self.__stack))
        c = self.__stack.pop()
        c = self.maxx.pop()



    def Max(self):
        assert(len(self.__stack))
        return self.maxx[-1]


if __name__ == '__main__':
    stack = StackWithMax()
    s = []

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            s.append(stack.Max())
        else:
            assert(0)
    for i in s:
        print(i)