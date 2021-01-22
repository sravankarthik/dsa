def check(maxx,digit):
    if int(digit+(maxx))>=int((maxx)+digit):
        return True
def largest_number(numbers):
    a=[]
    while numbers!=[]:
        maxx='0'
        for i in numbers:
            if check(maxx,i):
                maxx=i
        a.append(maxx)
        numbers.remove(maxx)
    summ=''
    for i in a:
        summ+=i
    return int(summ)











if __name__ == '__main__':
    n = int(input())
    input_numbers = input().split()
    assert len(input_numbers) == n
    print(largest_number(input_numbers))
