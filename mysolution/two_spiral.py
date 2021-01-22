import sys
#n = int(input())
n = 10
if n == 1:
    print([0, 0])
    sys.exit()
li = []
for i in range(n):
    li.append([])
for i in li:
    for j in range(n):
        i.append('*')
print(li)

direction = 0
left = 0
right = n-1
down = n-1
up = 0

while left <= right and up <= down:
    if direction == 0:
        for i in range(left, right+1):
            li[up][i] = 0
        up += 1
    elif direction == 1:
        for i in range(up, down+1):
            li[i][right] = 0
        right -= 1
        up += 1
    elif direction == 2:
        for i in range(right, left-1, -1):
            li[down][i] = 0
        down -= 1
        right -= 1
    elif direction == 3:
        for i in range(down, up-1, -1):
            li[i][left] = 0
        left += 1
        down -= 1
    if (direction + 1) % n == 0:
        li[up][left] = 0
        left += 1
    direction = (direction + 1) % n

for i in li:
    print(*i)