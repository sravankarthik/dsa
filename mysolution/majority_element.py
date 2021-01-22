import math
def majority_element_naive(elements):
    assert len(elements) <= 10 ** 5
    for e in elements:
        if elements.count(e) > len(elements) / 2:
            return 1

    return 0
def count(li,x):
    countt=0
    for i in li:
        if i==x:
            countt+=1
    return countt

def majority_element(elements,n):
    assert len(elements) <= 10 ** 5
    elements.sort()

    if n%2 != 0:
        mid=int((n-1)/2)
        if count(elements,elements[mid])>(n/2):
            return 1
    else:
        mid1=math.floor((n-1)/2)
        mid2=math.ceil((n-1)/2)
        if count(elements,elements[mid1])>(n/2):
            return 1
        elif count(elements,elements[mid2])>(n/2):
            return 1
    return 0





if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element(input_elements,input_n))
