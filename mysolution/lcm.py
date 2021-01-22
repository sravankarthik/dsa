def gcd(a,b):
    if b==0:
        return a
    x=a%b
    return gcd(b,x)


def lcm(a, b):
    assert 1 <= a <= 2 * 10 ** 9 and 1 <= b <= 2 * 10 ** 9
    return int((a*b)/gcd(a,b))






if __name__ == '__main__':
    input_a, input_b = map(int, input().split())
    print(lcm(input_a, input_b))
