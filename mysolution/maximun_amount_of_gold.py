from sys import stdin


def maximum_gold(capacity, weights):
    assert 1 <= capacity <= 10 ** 4
    assert 1 <= len(weights) <= 10 ** 3
    assert all(1 <= w <= 10 ** 5 for w in weights)

    if capacity in weights:
        return capacity
    li=[]
    weights.insert(0,0)
    for i in range(len(weights)):
        li.append([0])
    for i in li:
        for j in range(capacity):
            i.append(0)

    for i in range(1,len(weights)):
        for j in range(1,capacity+1):
            if weights[i]<=j:
                li[i][j]=max(li[i-1][j],weights[i]+li[i-1][j-weights[i]])
            else:
                li[i][j]=li[i-1][j]

    return li[len(weights)-1][capacity]



'''print(maximum_gold(10, [1, 4, 8]))
print(maximum_gold(7,[1,3,4,5]))
print(maximum_gold(20, [5, 7, 12, 18]))
print(maximum_gold(10, [3, 5, 3, 3, 5]))'''





if __name__ == '__main__':
    input_capacity, n, *input_weights = list(map(int, stdin.read().split()))
    assert len(input_weights) == n

    print(maximum_gold(input_capacity, input_weights))
