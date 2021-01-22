def lcs2(first_string, second_string):
    #assert len(first_sequence) <= 100
    #assert len(second_sequence) <= 100

    li1=list(first_string)
    li2=list(second_string)
    li1.insert(0,0)
    li2.insert(0,0)
    li=[]

    for i in range(len(li2)):
        li.append([])
        for j in range(len(li1)):
            li[i].append(0)
    for j in range(1,len(li1)):
        for i in range(1,len(li2)):

            if li1[j]==li2[i]:

                li[i][j]=li[i-1][j-1]+1

            else:
                li[i][j]=max(li[i-1][j],li[i][j-1])
    return li[len(li2)-1][len(li1)-1]

def lcs3(first_sequence, second_sequence, third_sequence):
    assert len(first_sequence) <= 100
    assert len(second_sequence) <= 100
    assert len(third_sequence) <= 100

    a=lcs2(first_sequence,second_sequence)
    b=lcs2(second_sequence,third_sequence)
    c=lcs2(third_sequence,first_sequence)
    return min(a,b,c)


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    q = int(input())
    c = list(map(int, input().split()))
    assert len(c) == q

    print(lcs3(a, b, c))
