from random import randint


def partition3(array, left, right):

    li = array
    b = li[left]
    j=left
    for i in range(left+1,right+1):
        if li[i] <= b:
            j += 1
            li[j],li[i]=li[i],li[j]
    li[left],li[j]=li[j],li[left]


    k=left
    for i in range(k,j):
        if li[i] < li[j]:
            li[i],li[k]=li[k],li[i]
            k+=1




    return j,k







def randomized_quick_sort(array, left, right):
    if left >= right:
        return
    k = randint(left, right)
    array[left], array[k] = array[k], array[left]
    m,k = partition3(array,left,right)
    randomized_quick_sort(array,left,k)
    randomized_quick_sort(array,m+1,right)
    return array



if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    randomized_quick_sort(elements, 0, len(elements) - 1)
    print(*elements)
