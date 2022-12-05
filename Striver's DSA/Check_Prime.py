import math


def check_prime_bruteforce(m):
    if(m==0 | m==1):
        return'Not a prime'

    for i in range(2,m//2):
        if(m%i==0):
            return 'Not a prime'
    return 'Prime'


def check_prime(m):
    Range = int(math.sqrt(m))
    for i in range(2, Range+1):
        if(m%i==0):
            return 'not a prime'
    return 'prime'



print(check_prime_bruteforce(36))
print(check_prime(37))