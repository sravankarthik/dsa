def quick(a,l,r):
    if l >= r:
        return a
    m = partition(a,l,r)
    quick(a,l,m-1)

    quick(a,m+1,r)
    return a

def partition(a,l,r):
    x = a[l]
    j=l
    for i in range(l+1,r+1):
        if a[i] <= x:
            j+=1
            a[j],a[i]=a[i],a[j]
    a[l],a[j]=a[j],a[l]
    return j
if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    quick(elements, 0, len(elements) - 1)
    print(*elements)
