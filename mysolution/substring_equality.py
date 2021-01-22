import sys


def hash_value(s):
    x = 31
    p = 101
    summ = 0
    for i in s:
        summ = (summ * x + ord(i)) % p
    return summ


class Solver:
    dicty = {}

    def __init__(self, word):
        self.word = word
        self.length = len(word)

    def ask(self, a, b, l):
        if a == b:
            return True
        #else:
            #return hash_value(self.word[a:a+l]) == hash_value(self.word[b:b+l])
        if l in self.dicty.keys():
            return self.dicty[l][a] == self.dicty[l][b]

        si = []
        p = 101
        x = 31
        y = 1
        for i in range(l-1):
            y = (y * x) % p
        for i in range(self.length - l+1):
            si.append(0)
        si[0] = hash_value(self.word[:l])

        for i in range(self.length-l):
            si[i+1] = (x * (si[i] - ord(self.word[i]) * y) + ord(self.word[i + l])) % p
        self.dicty[l] = si
        print(self.dicty)

        if si[a] == si[b]:
            return True
        else:
            return False


s = input()
q = int(sys.stdin.readline())
solver = Solver(s)
for i in range(q):
    a, b, l = map(int, sys.stdin.readline().split())
    print("Yes" if solver.ask(a, b, l) else "No")
