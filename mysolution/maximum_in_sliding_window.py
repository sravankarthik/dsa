def max_sliding_window(li, m):
    arr = li[:m]
    arr1 = li[:m]

    i = m - 1
    s = []
    arr1 = [i[0] for i in sorted(enumerate(arr1), key=lambda x: x[1])]
    arr1.reverse()
    g = arr1

    s.append(arr[g[0]])
    while i < len(li) - 1:

        i += 1
        q = arr.pop(0)
        arr.append(li[i])
        if i - m in g:
            g.remove(i - m)
        if len(g) == 0 or li[i] >= li[g[0]]:
            g = [i]
        elif li[i] <= li[g[0]]:
            for o in range(len(g)):
                if li[g[o]] < li[i]:
                    g = g[:o]
                    break
            g.append(i)
        s.append(li[g[0]])

    return s


'''if __name__ == '__main__':
    n = int(input())
    input_sequence = []
    x = input()
    x = x.split()
    y = []
    for i in x:
        y.append(int(i))
    window_size = int(input())

    print(*max_sliding_window(y, window_size))'''
if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    print(*max_sliding_window(input_sequence, window_size))
