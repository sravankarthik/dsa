class node:
    def __init__(self, value):
        self.value = value
        self.leaf = False


li = [-1] * 31
for i in range(1, 14, 2):
    li[i] = node(0)
for i in range(14, 31, 2):
    li[i] = node(0)
    li[i].leaf = True
for i in range(2, 15, 2):
    li[i] = node(1)
for i in range(15, 31, 2):
    li[i] = node(1)
    li[i].leaf = True
arr = [-1] * 15 + 'a b c d e f g h i j k l m n o p'.split()

'''s = '00001111'
ans = '''''
li[0] = node(-1)
'''point = 0
for i in s:
    if int(i) == 0:
        point = 2 * point + 1
    else:
        point = 2 * point + 2
    if li[point].leaf:
        ans += arr[point]
        point = 0
print(ans)'''
T = int(input())
for i in range(T):
    ans = ''
    d = input()
    s = input()
    point = 0
    for i in s:
        if int(i) == 0:
            point = 2 * point + 1
        else:
            point = 2 * point + 2
        if li[point].leaf:
            ans += arr[point]
            point = 0
    print(ans)