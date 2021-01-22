li = {}
for i in range(int(input('the number of things:'))):
    x, y = input().split()
    li[int(x)] = y
print(li)
n = int(input())
for i in range(1, n + 1):
    count = 0
    for j in li.keys():
        if i % j == 0:
            print(li[j], end=' ')
            count = 1
    if count == 0:
        print(i)
    else:
        print()
