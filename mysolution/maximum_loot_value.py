from sys import stdin


def maximum_loot_value(capacity, weights, prices):
    assert 0 <= capacity <= 2 * 10 ** 6
    assert len(weights) == len(prices)
    assert 1 <= len(weights) <= 10 ** 3
    assert all(0 < w <= 2 * 10 ** 6 for w in weights)
    assert all(0 <= p <= 2 * 10 ** 6 for p in prices)
    li = []
    bag = 0
    price = 0
    w_sum=0
    p_sum=0
    for i in weights:
        w_sum+=i
    for i in prices:
        p_sum+=i
    if w_sum <= capacity:
        return float(p_sum)

    for i in range(len(weights)):
        li.append(prices[i]/weights[i])

    while capacity>0 and len(li)!=0 :
        maxx=0
        indexx=li[0]
        for i in li:
            if i>=maxx:
                maxx=i
                indexx=li.index(i)
        li[indexx]=0

        if weights[indexx]<=capacity:
            capacity-=weights[indexx]
            price+=prices[indexx]

        else:
            price+=(capacity*prices[indexx]/weights[indexx])
            break

    return price







#print(maximum_loot_value(16,[6,10,3,5,1,3],[6,2,1,8,3,5]))

#if __name__ == "__main__":
    #data = list(map(int, stdin.read().split()))
    #n, input_capacity = data[0:2]
    #input_prices = data[2:(2 * n + 2):2]
    #input_weights = data[3:(2 * n + 2):2]
    #opt_value = maximum_loot_value(input_capacity, input_weights, input_prices)
    #print("{:.10f}".format(opt_value))

if __name__ == "__main__":
    value_list = []
    weight_list = []

    #The first line of the input contains the number 𝑛 of items and the capacity 𝑊 of a knapsack.
    #The next 𝑛 lines define the values and weights of the items.

    n , capacity = map(int, input().split())

    for i in range (n):
        value , weight = map(int, input().split())
        value_list.append(value)
        weight_list.append(weight)
print("{:.10f}".format(maximum_loot_value(capacity,weight_list, value_list)))
