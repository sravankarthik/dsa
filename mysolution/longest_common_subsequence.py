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

    '''for i in range(len(li[0])):
        li[0][i]=0
    for i in range(len(li)):
        li[i][0]=0'''


    for j in range(1,len(li1)):
        for i in range(1,len(li2)):

            if li1[j]==li2[i]:

                li[i][j]=li[i-1][j-1]+1

            else:
                li[i][j]=max(li[i-1][j],li[i][j-1])
    return li[len(li2)-1][len(li1)-1]



    '''
    for i in li:
        print(i)
    i=len(li2)-1
    j=len(li1)-1
    del1=[]
    del2=[]
    while i!=0 and j!=0:
        if li[i][j]==li[i-1][j-1] and li1[j]==li2[i]:
            i-=1
            j-=1

        else:
            minn=min(li[i-1][j],li[i][j-1],li[i-1][j-1])+1
            if li[i-1][j-1]+1==li[i][j] and li[i-1][j-1]+1==minn:
                del1.append(j)
                del2.append(i)
                i-=1
                j-=1
                continue
            elif li[i-1][j]+1==li[i][j] and li[i-1][j]+1==minn:
                del2.append(i)
                i-=1
                continue
            elif li[i][j-1]+1==li[i][j] and li[i][j-1]+1==minn:
                del1.append(j)
                j-=1

                continue
    print(del1,del2)
    soln1=[]
    soln2=[]
    print()

    for i in range(1,len(li1)):
        if i not in del1:
            soln1.append(li1[i])
    for i in range(1,len(li2)):
        if i not in del2:
            soln2.append(li2[i])
    print(soln1,soln2)

    soln3=[]
    for i in soln1:
        if i in soln2:
            soln3.append(i)
    return(len(soln3))'''







if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    print(lcs2(a, b))
