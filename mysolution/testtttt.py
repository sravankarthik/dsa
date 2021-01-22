import sys


def saif(li, r, c, n):
    for i in range(c):
        if li[r][i] == 1:
            return False
    for i, j in zip(range(r, -1, -1), range(c, -1, -1)):
        if li[i][j] == 1:
            return False
    for i, j in zip(range(r, n, 1), range(c, -1, -1)):
        if li[i][j] == 1:
            return False

    return True


def check(li, c, n):
    if c >= n:
        return True
    for i in range(n):
        if saif(li, i, c, n):
            li[i][c] = 1
            if check(li, c + 1, n) == True:
                return True
            li[i][c] = 0
    return False


if __name__ == '__main__':
    n = int(input())
    if n == 1:
        print([0, 0])
        sys.exit()
    li = []
    for i in range(n):
        li.append([])
    for i in li:
        for j in range(n):
            i.append(0)
    if check(li, 0, n) == False:
        print([])
        sys.exit()
    result = []
    for i in range(n):
        for j in range(n):
            if li[i][j] == 1:
                result.append([i, j])
    print(result)
