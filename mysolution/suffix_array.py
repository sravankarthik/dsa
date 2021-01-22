def sort_characters(s):
    li = []
    j = 0
    for i in s:
        li.append([i, j])
        j += 1
    li.sort(key=lambda x: x[0])
    result = []
    for i in li:
        result.append(i[1])
    return result


def compute_char_classes(s, order):
    count = 1
    c = [0] * len(order)
    c[order[0]] = count
    for i in range(1, len(order)):
        if s[order[i - 1]] == s[order[i]]:
            c[order[i]] = count
        else:
            count += 1
            c[order[i]] = count
    return c


'''def sort_double(s, l, order, c):
    a = len(s)
    count = [0] * a
    new_order = [0] * a
    for i in range(a):
        count[c[i]] += 1
    for j in range(1, a):
        count[j] += count[j - 1]
    for i in range(a-1, 0, -1):
        start = (order[i] - l + a) % a
        cl = c[start]
        count[cl] -= 1
        new_order[count[cl]] = start
    return new_order


def update_class(neworder, c, l):
    n = len(neworder)
    newclass = [0] * n
    newclass[neworder[0]] = 0
    for i in range(1, n):
        cur = neworder[i]
        prev = neworder[i - 1]
        mid = (cur + l) % n
        mid_prev = (prev + l) % n
        if c[cur] != c[prev] or c[mid] != c[mid_prev]:
            newclass[cur] = newclass[prev] + 1
        else:
            newclass[cur] = newclass[prev]
    return newclass


def build_suffix_array(s):
    order = sort_characters(s)
    c = compute_char_classes(s, order)
    print(order, c)
    l = 1
    while l < len(s):
        order = sort_double(s, l, order, c)
        c = update_class(order, c, l)
        l *= 2
    return order '''


def test(s):
    q = len(s)
    order = sort_characters(s)
    li = compute_char_classes(s, order)
    print(li)
    boo = True
    j = 1
    count = 0
    while boo:
        arr = []
        for i in range(q-j):
            arr.append(((li[i], li[i+j]), i))
        for i in range(q-j, q):
            arr.append(((li[i], -1), i))
        if count >= q-1:
            boo = False
        arr.sort(key=lambda x: x[0])
        print(arr)
        result = [0] * q
        count = 0
        result[arr[0][1]] = count
        for i in range(1, q):
            if arr[i-1][0] == arr[i][0]:
                result[arr[i][1]] = count
            else:
                count += 1
                result[arr[i][1]] = count
            if count >= q - 1:
                boo = False
                t = []
                for g in range(q):
                    t.append((result[g], g))
                t.sort(key=lambda x: x[0])
                e =[]
                for g in t:
                    e.append(g[1])
                return e
        print(result)
        li = result
        j *= 2
    return li


#print(test('trollolol'))
#print(test('AAA$'))
#print(test('GAGAGAGA$'))
#print(test('AACGATAGCGGTAGA$'))
print(test('ababaa$'))