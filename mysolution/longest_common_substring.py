# python3

import sys
from collections import namedtuple

Answer = namedtuple('answer_type', 'i j len')


def solve(s, t):
    ans = Answer(0, 0, 0)
    li = []
    maxx = 0
    i_maxx = 0
    j_maxx = 0
    for i in range(len(t) + 1):
        li.append([])
    for i in li:
        for j in range(len(s) + 1):
            i.append(0)

    for i in range(1, len(t) + 1):
        for j in range(1, len(s) + 1):
            if t[i - 1] == s[j - 1]:
                li[i][j] = li[i - 1][j - 1] + 1
                if li[i][j] >= maxx:
                    maxx = li[i][j]
                    i_maxx = i
                    j_maxx = j

    # for i in li:
    # print(i)
    if maxx == 0:
        ans = Answer(0, len(t) - 1, 0)
        return ans
    ans = Answer(j_maxx - maxx, i_maxx - maxx, maxx)
    return ans


# solve('abcdaf','zbcdf')
# solve('babbaab','aabaa')
print(solve('zxabcdezy','yzabcdezx'))


for line in sys.stdin.readlines():
    s, t = line.split()
    ans = solve(s, t)
    print(ans.i, ans.j, ans.len)
