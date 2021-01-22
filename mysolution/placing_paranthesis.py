import math
def compare(i,j,maxx,minn,li):
    min_=10**6
    max_=-10**6

    for k in range(i,j):
        if li[k]=="*":
            a=maxx[i][k]*maxx[k+1][j]
            b=maxx[i][k]*minn[k+1][j]
            c=minn[i][k]*maxx[k+1][j]
            d=minn[i][k]*minn[k+1][j]
            min_=min(min_,a,b,c,d)
            max_=max(max_,a,b,c,d)
        elif li[k]=="+":
            a=maxx[i][k]+maxx[k+1][j]
            b=maxx[i][k]+minn[k+1][j]
            c=minn[i][k]+maxx[k+1][j]
            d=minn[i][k]+minn[k+1][j]
            min_=min(min_,a,b,c,d)
            max_=max(max_,a,b,c,d)
        elif li[k]=="-":
            a=maxx[i][k]-maxx[k+1][j]
            b=maxx[i][k]-minn[k+1][j]
            c=minn[i][k]-maxx[k+1][j]
            d=minn[i][k]-minn[k+1][j]
            min_=min(min_,a,b,c,d)
            max_=max(max_,a,b,c,d)
    return min_,max_




def find_maximum_value(dataset):
    assert 1 <= len(dataset) <= 29


    maxx=[]
    minn=[]
    li=[]
    li.append(0)
    for i in dataset:
        if i=="*" or i=="+" or i=="-":
            li.append(i)

    for i in range(math.ceil(len(dataset)/2)+1):
        maxx.append([0])
        minn.append([0])
    for i in maxx:
        for j in range(math.ceil(len(dataset)/2)):
            i.append(0)
    for i in minn:
        for j in range(math.ceil(len(dataset)/2)):
            i.append(0)

    i=1
    j=1
    for k in range(0,len(dataset),2):
        minn[i][j]=int(dataset[k])
        maxx[i][j]=int(dataset[k])
        i+=1
        j+=1

    for j in range(1,len(maxx[0])-1):
        for i in range(1,len(maxx[0])-j):
            minn[i][j+i],maxx[i][j+i]=compare(i,j+i,maxx,minn,li)
    return maxx[1][len(maxx[1])-1]






#print(find_maximum_value("8-5*3"))
#print(find_maximum_value("5-8+7*4-8+9"))

if __name__ == "__main__":
    print(find_maximum_value(input()))
