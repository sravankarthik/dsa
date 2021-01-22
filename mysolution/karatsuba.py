import math


def karatsuba(x, y):

    if x < 10 and y < 10:
        return x*y                                                                       #base case

    n = max(len(str(x)), len(str(y)))
    m = int(math.ceil(n/2))

    x_h = int(x/10**m)
    x_l = int(x%10**m)

    y_h = int(y/10**m)
    y_l = int(y%10**m)

    s1 = karatsuba(x_h, y_h)
    s2 = karatsuba(x_l, y_l)
    s3 = karatsuba(x_h+x_l, y_h+y_l)
    s4 = s3-s1-s2

    return int(s1*10**n+s4*10**m+s2)
