dicty={1:[1],2:[1,2],3:[1,3]}
def compute_operations(n):
    assert 1 <= n <= 10 ** 6
    if n in dicty.keys():
        return dicty[n]
    else:
        dicty[n]=[]
    for i in range(4,n+1):
        #a=[0]*(10**6)
        a=compute_operations(i-1)
        d=a
        count=0

        if i%2==0:
            b=compute_operations(i/2)
            if len(b)<len(a):
                d=b
                count=1
        if i%3==0:
            c=compute_operations(i/3)
            if count==1 and len(c)<len(b):
                d=c
            elif len(c)<len(a):
                d=c
        '''d=min(len(a),len(b),len(c))

        if d==len(a):

            d=a
        elif d==len(b):

            d=b
        elif d==len(c):

            d=c'''

        dicty[i]=d
        dicty[i]=dicty[i]+[i]

    return dicty[n]


if __name__ == '__main__':
    input_n = int(input())
    output_sequence = compute_operations(input_n)
    print(len(output_sequence)-1)
    print(*output_sequence)
