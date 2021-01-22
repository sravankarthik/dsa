def merge(a,b):
    li = []
    while len(a)!=0 and len(b)!=0:
        if a[0]<=b[0]:
            li.append(a[0])
            x=a.pop(0)
        elif b[0]<a[0]:
            li.append(b[0])
            x=b.pop(0)

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
