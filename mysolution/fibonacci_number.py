dicty={}
def fibonacci_number(n):
    if n in dicty:
        return dicty[n]

    if n==0:
        x=0
    elif n==1:
        x=1
    elif n>1:
        x=fibonacci_number(n-1)+fibonacci_number(n-2)
    dicty[n]=x
    return x



if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))
