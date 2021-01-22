dicty = {}
def counting_sort(a):
    for i in a:
        if i in dicty.keys() and dicty[i]>=1:
            dicty[i]+=1
            continue
        dicty[i]=1
    li=dicty.keys()
    s=max(li)
    f=min(li)
    k=[]
    for i in range(f,s+1):
        if i in li:
            for j in range(dicty[i]):
                k.append(i)
    return k


#print(counting_sort([2,3,9,2,9]))
if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n

    x=counting_sort(elements)
    for i in x:
        print(i,end=' ')

