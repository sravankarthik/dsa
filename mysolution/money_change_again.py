dicty={0:0,4:1,3:1,1:1}
'''for i in range(100):
    if i not in dicty.keys():
        dicty[i]=10**6'''


def change(money,li=[4,3,1]):
    if money in dicty.keys():
        return dicty[money]
    else:
        dicty[money]=10**6

    for i in li:
        if money>=i:
            minn=change(money-i)+1

            if minn<dicty[money]:
                dicty[money]=minn


    return dicty[money]





if __name__ == '__main__':
    amount = int(input())
    print(change(amount))
