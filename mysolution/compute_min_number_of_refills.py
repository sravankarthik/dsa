def compute_min_number_of_refills(d, m, stops):
    assert 1 <= d <= 10 ** 5
    assert 1 <= m <= 400
    assert 1 <= len(stops) <= 300
    assert 0 < stops[0] and all(stops[i] < stops[i + 1] for i in range(len(stops) - 1)) and stops[-1] < d

    count = 0
    curr = 0
    stops.insert(0, 0)
    stops.append(d)
    n = len(stops) - 2
    while curr <= n:
        l = curr
        while curr <= n and stops[curr + 1] - stops[l] <= m:
            curr += 1
        if curr == l:
            return -1
        elif curr <= n:
            count += 1
    return count


if __name__ == '__main__':
    input_d = int(input())
    input_m = int(input())
    input_n = int(input())
    input_stops = list(map(int, input().split()))
    assert len(input_stops) == input_n

    print(compute_min_number_of_refills(input_d, input_m, input_stops))
