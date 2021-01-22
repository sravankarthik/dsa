dicty = {0: 0, 1: 1, 2: 1}
a = 0
b = 1
for i in range(2, 60):
    summ = a + b
    x = str(summ)
    x = int(x[len(x) - 1])
    a = b
    b = x
    dicty[i] = x


def last_digit_of_the_sum_of_squares_of_fibonacci_numbers(n):
    # assert 0 <= n <= 10 ** 18

    y = dicty[n % 60] * (dicty[(n + 1) % 60])
    y = str(y)
    y = int(y[len(y) - 1])
    return y


if __name__ == '__main__':
    input_n = int(input())
    print(last_digit_of_the_sum_of_squares_of_fibonacci_numbers(input_n))
