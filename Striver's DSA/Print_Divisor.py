
from cmath import sqrt
import math


def list_divisor_bruteforce(m):
    list = []
    

    half = m//2
    for i in range(1,half + 1):
        if(m%i==0):
            list.append(i)
    list.append(m)
    return list


def list_divisor(m):
    Range = int(math.sqrt(m))
    lst = []
    for i in range(1, Range+1):
        if(m%i==0):
            lst.append(i)
            if(m/i!=i):
                lst.append(int(m/i))
    return lst


    




print(list_divisor_bruteforce(35))
print(list_divisor(35))