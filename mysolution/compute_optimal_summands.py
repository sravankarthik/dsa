import math
def compute_optimal_summands(n):
    assert 1 <= n <= 10 ** 9
    summands = []
    x=(-1+(1+8*n)**(0.5))/2
    y=(-1-(1+8*n)**(0.5))/2
    maxx=max(x,y)
    minn=min(x,y)
    maxx=math.floor(maxx)
    minn=math.ceil(minn)
    li=[]

    for i in range(maxx+1,max(0,minn),-1):
        if (i*i+i-2*n) <= 0:
            z=i

            break
    summ=0
    for i in range(1,z):
        li.append(i)
        summ+=i
    li.append(n-summ)
    return li







if __name__ == '__main__':
    input_n = int(input())
    output_summands = compute_optimal_summands(input_n)
    print(len(output_summands))
    print(*output_summands)

