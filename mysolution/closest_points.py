# python3
from collections import namedtuple
from itertools import combinations
from math import sqrt


Point = namedtuple('Point', 'x y')


def distance_squared(first_point, second_point):
    return ((first_point[0] - second_point[0]) ** 2 + (first_point[1] - second_point[1]) ** 2)


def minimum_distance_squared(points):


    if len(points)==2:
        return distance_squared(points[0],points[1])
    '''elif len(points)==3:
        k1=distance_squared(points[0],points[1])
        k2=distance_squared(points[1],points[2])
        k3=distance_squared(points[0],points[2])
        return min(k1,k2,k3)'''

    if len(points)==1:
         return 10**6


    n=int(len(points)/2)
    a=minimum_distance_squared(points[:n])
    b=minimum_distance_squared(points[n:])


    d=min(a,b)
    if d == 0:
        return 0

    li_r=[]
    li_l=[]
    li_r.append(points[n])
    for i in range(n+1,len(points)):
        if abs(points[n][0]-points[i][0])<d:
            li_r.append(points[i])

    for i in range(n-1,-1,-1):
        if abs(points[n][0]-points[i][0])<d:
            li_l.append(points[i])
    li_l.reverse()
    li=li_l+li_r
    li.sort(key=lambda x:x[1])
    #li_r.sort(key=lambda x:x[1])
    #li_l.sort(key=lambda x:x[1])
    '''for i in range(len(li)):
        for j in range(i+1,len(li)):
            if abs(li[i][1]-li[j][1])<d:
                d=min(d,distance_squared(li[i],li[j]))
            else:
                break'''
    for i in range(len(li)-1):
        if (li[i] in li_l and li[i+1] in li_r) or (li[i] in li_r and li[i+1] in li_l):
            if abs(li[i][1]-li[i+1][1])<d:
                u = distance_squared(li[i],li[i+1])
                if u<d:
                    d = u










    '''for i in range(1,len(li)):

        d=min(d,distance_squared(li[0],li[i]))
    for i in range(len(li)):
        for j in range(i,len(li)):
            x=distance_squared(li[i],li[j])
            if x!=0:
                d=min(d,x)'''



    return d

#print(minimum_distance_squared([[1,1],[2,2],[3,3]]))



if __name__ == '__main__':
    input_n = int(input())
    input_points = []
    for _ in range(input_n):
        x, y = map(int, input().split())
        input_point = Point(x, y)

        input_points.append(input_point)
        input_points.sort()

    print("{0:.9f}".format(sqrt(minimum_distance_squared(input_points))))
