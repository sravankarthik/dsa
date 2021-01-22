# python3

from itertools import product
from sys import stdin
def part(s,n,a,b,c):
    if a==0 and b==0 and c==0:
        return 1
    if n<0:
        return 0
    aa=0
    if a-s[n]>=0:
        aa=part(s,n-1,a-s[n],b,c)
    bb=0
    if aa==0 and b-s[n]>=0:
        bb=part(s,n-1,a,b-s[n],c)
    cc=0
    if aa==0 and bb==0 and  c-s[n]>=0:
        cc=part(s,n-1,a,b,c-s[n])
    return aa or bb or cc



def partition3(values):
    assert 1 <= len(values) <= 20
    assert all(1 <= v <= 30 for v in values)
 

    summ=0
    for i in values:
        summ+=i
    if summ%3!=0:
        return 0
    x=int(summ/3)
    return part(values,len(values)-1,x,x,x)







if __name__ == '__main__':
    input_n, *input_values = list(map(int, stdin.read().split()))
    assert input_n == len(input_values)

    print(partition3(input_values))
