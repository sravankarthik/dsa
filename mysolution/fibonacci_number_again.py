def fibo(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    a = 1
    b = 1
    for i in range(3, n + 1):
        summ = a + b
        a = b
        b = summ
    return summ


def fibonacci_number_again(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1

    a = 1
    b = 1
    li = []
    dicty = {0: 0, 1: 1, 2: 1}
    if m != 2:
        for i in range(3, 10 ** 18 + 1):
            summ = a + b
            a = b
            b = summ
            x = summ % m
            dicty[i] = summ

            li.append(x)
            if li[len(li) - 1] == 1 and li[len(li) - 2] == 0:
                y = len(li) + 1
                break
    elif m == 2:
        y = 2
        z = n % 3
        return fibo(z) % m

    z = n % y
    return dicty[z] % m


if __name__ == '__main__':
    input_n, input_m = map(int, input().split())
    print(fibonacci_number_again(input_n, input_m))
