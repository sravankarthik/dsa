n=int(input())
line=input()
#line=line.split(" ")
#line=line[:n]
#line=list(map(int,line))
#line.sort()
#line.reverse()
#print(int(line[len(line)-1])*int(line[len(line)-2]))

def maximise(n,line):
    line=line.split(" ")
    line=line[:n]
    line=list(map(int,line))
    maxx1=0
    maxx2=0
    a=0
    b=0
    for i in range(n):
        maxx1=line[i]
        for j in range(1,n):
            if maxx1<line[j]:
                maxx1=line[j]
                line[i],line[j]=line[j],line[i]
        maxx2=line[i+1]
        for j in range(2,n):
            if maxx2<line[j]:
                maxx2=line[j]
                line[i],line[j]=line[j],line[i]
        break
    return (maxx1*maxx2)
    
print(maximise(n,line))
        
        
        
    


