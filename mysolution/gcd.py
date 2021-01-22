def gcd(a, b):
    assert 0 <= a <= 2 * 10 ** 9 and 0 <= b <= 2 * 10 ** 9

    # if b == 0:
    # return a
    # x=a%b
    # return gcd(b,x)
    while b != 0:
        x = b
        b = a % b
        a = x
    return a



if __name__ == '__main__':
    input_a, input_b = map(int, input().split())
    print(gcd(input_a, input_b))
