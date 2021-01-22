def last_digit_of_fibonacci_number(n):
    assert 0 <= n <= 10 ** 7
    # 1 1 2 3 5
    if n == 1:
        return 1
    elif n==2:
        return 1

    a=1
    b=1
    for i in range(2,n):
        summ=a+b
        #print(summ)
        x=str(summ)
        x=int(x[len(x)-1])
        a=b
        b=x
    return x



if __name__ == '__main__':
    input_n = int(input())
    print(last_digit_of_fibonacci_number(input_n))
