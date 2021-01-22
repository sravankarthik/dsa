def money_change(money):
    assert 0 <= money <= 10 ** 3
    if money%10==0:
        return int(money/10)
    else:
        x=money%10
        if x<5:
            return int(int(money/10)+x)
        elif x==5:
            return int(int(money/10)+1)
        else:
            return int(int(money/10)+1+(x-5))


if __name__ == '__main__':
    input_money = int(input())
    print(money_change(input_money))
