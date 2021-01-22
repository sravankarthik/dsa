import suffix_array


class node:
    def __init__(self, start_index, length):
        self.start_index = start_index
        self.length = length
        self.depth = 0
        self.parent = None
        self.childern = []


# s = input()
s = 'GTAGT$'
l = len(s)
li = suffix_array.test(s)
print(li)
lcp_arr = [0] * (len(s) - 1)
count = 0
i = 0


def lcp(x, y, s):
    l = len(s)
    x = x % l
    y = y % l
    boo = True
    count = 0
    while boo:
        if s[x] == s[y]:
            x = (x + 1) % l
            y = (y + 1) % l
            count += 1
        else:
            boo = False
            return count
    return count


while count != l - 1:
    count += 1
    lcp_arr[i] = lcp(li[i], li[(i + 1) % l], s)
    i = (i + 1) % l
print(lcp_arr)

root = node(None, None)
a = node(li[0], l - li[0])
a.depth = 1
a.parent = root
root.childern.append(a)
point = a

for i in range(len(lcp_arr)):
    while point.depth != lcp_arr[i] and lcp_arr[i] <= point.depth:
        point = point.parent
    if point.childern:
        a = node(li[i + 1]+point.depth, l - li[i + 1])
        a.parent = point
        a.depth = point.depth + 1
        point.childern.append(a)
        point = a
    else:
        a = node(li[i + 1] + lcp_arr[i], l - li[i + 1] - lcp_arr[i])
        a.parent = point
        a.depth = point.depth + 1
        point.childern.append(a)
        b = node(point.start_index + lcp_arr[i] - point.depth + 1, l - (point.start_index + lcp_arr[i] - point.depth + 1))
        b.parent = point
        b.depth = point.depth + 1
        point.childern.append(b)
        point.length = lcp_arr[i] - point.depth + 1
        point = a
pass