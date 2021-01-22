


























































































































# python3
def hash_value(s):
    x = 256
    p = 101

    j = 0
    summ = 0
    for i in s:
        summ = (summ + ord(i) * (x ** j)) % p
        j += 1
    return summ


def read_input():
    return (input().rstrip(), input().rstrip())


def print_occurrences(output):
    print(' '.join(map(str, output)))


def get_occurrences(pattern, text):
    p = len(pattern)
    t = len(text)
    x = 13
    w = 0
    s = 0
    pr = 101
    y = 1
    for i in range(p):
        w = (w * x + ord(pattern[i])) % pr
        s = (s * x + ord(text[i])) % pr
    if w == s:
        print(0, end=' ')
    #print(w, s)
    for i in range(p - 1):
        y = (y * x) % pr
    for i in range(t - p):
        s = (x * (s - ord(text[i]) * y) + ord(text[i + p])) % pr
        #print(s)
        if s == w and pattern == text[i + 1:i + p + 1]:
            print(i + 1, end=' ')
    #return []


if __name__ == '__main__':
    get_occurrences(*read_input())
