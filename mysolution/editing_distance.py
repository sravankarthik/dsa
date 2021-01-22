def edit_distance(first_string, second_string):
    li1=list(first_string)
    li2=list(second_string)
    li1.insert(0,0)
    li2.insert(0,0)
    li=[]

    for i in range(len(li2)):
        li.append([])
        for j in range(len(li1)):
            li[i].append(0)

    for i in range(len(li[0])):
        li[0][i]=i
    for i in range(len(li)):
        li[i][0]=i

    for j in range(1,len(li1)):
        for i in range(1,len(li2)):

            if li1[j]==li2[i]:

                li[i][j]=li[i-1][j-1]

            else:
                li[i][j]=min(li[i-1][j],li[i][j-1],li[i-1][j-1])+1


    return li[len(li2)-1][len(li1)-1]





if __name__ == "__main__":
    print(edit_distance(input(), input()))
