# python3
import sys


def InverseBWT(bwt):
    li = []
    l = len(bwt)
    bwt = list(bwt)
    for i in bwt:
        li.append(i)
    li.sort()
    print(li, bwt)
    while len(li[0]) != l:
        for i in range(l):
            li[i] = bwt[i] + li[i]
        li.sort()
    print(li)
    return li[0][1:] + li[0][0]


print(InverseBWT('annb$aa'))
print(InverseBWT('AC$A'))
print(InverseBWT('AGGGAA$'))

if __name__ == '__main__':
    bwt = sys.stdin.readline().strip()
    print(InverseBWT(bwt))
