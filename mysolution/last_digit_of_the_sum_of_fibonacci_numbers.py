def last_digit_of_the_sum_of_fibonacci_numbers(n):
    assert 0 <= n <= 10 ** 18

    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    a = 1
    b = 1
    t = 2
    dicty = {0: 0, 1: 1, 2: 2}
    for i in range(3, 60):
        summ = a + b
        a = b
        b = summ
        summ = str(summ)
        summ = int(summ[len(summ) - 1])
        t = t + summ
        t = str(t)
        t = int(t[len(t) - 1])
        dicty[i] = t
    x = n % 60
    return dicty[x]


if __name__ == '__main__':
    input_n = int(input())
    print(last_digit_of_the_sum_of_fibonacci_numbers(input_n))
