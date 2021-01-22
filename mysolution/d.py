n = int(input())
li = []
count = 0
#for i in range(n):
    #li.append(list(map(int, input().split())))
for i in range(n):
    li.append([int(j) for j in input().split()])
for i in li:
    if sum(i) >= 2:
        count += 1
print(count)