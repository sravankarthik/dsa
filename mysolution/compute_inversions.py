from itertools import combinations


def compute_inversions_naive(a):
    number_of_inversions = 0
    for i, j in combinations(range(len(a)), 2):
        if a[i] > a[j]:
            number_of_inversions += 1
    return number_of_inversions


def compute_inversions(a):
    b=mergesort(a)

    return dicty[0]

















dicty={0:0}
def merge(a, b):
    li = []
    mid=len(a)
    i = 0
    while len(a)!=0 and len(b)!=0:
        if a[0]<=b[0]:
            li.append(a[0])
            x = a.pop(0)
            i+=1

        elif b[0]<a[0]:
            li.append(b[0])
            x = b.pop(0)
            dicty[0]+=(mid-i)




        if len(a)==0:
            li = li+b
        elif len(b)==0:
            li = li+a

    return li



def mergesort(x):

    if len(x)==1:
        return x
    n=len(x)
    n=int(n/2)
    a=mergesort(x[:n])
    b=mergesort(x[n:])
    q=merge(a,b)
    return q


mergesort([8,7,6,5,4,3,2,1])

if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    print(compute_inversions(elements))

