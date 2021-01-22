def prefix(s):
    li = [0]
    border = 0
    for i in range(1, len(s)):
        while border > 0 and s[i] != s[border]:
            border = li[border - 1]
        if s[i] == s[border]:
            border += 1
        else:
            border = 0
        li.append(border)
    return li


def knuth_morris_pratt(s, p):
    final = p + '$' + s
    li = prefix(final)
    print(li)
    x = len(p)
    count = []
    for i in range(len(p), len(final)):
        if li[i] == x:
            count.append(i-2*x)
    return count


print(knuth_morris_pratt('abracadabra', 'abra'))
print(knuth_morris_pratt('GATATATGCATATACTT', 'ATAT'))
