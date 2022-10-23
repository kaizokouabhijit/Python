def gcd_bruteForce(m, n):

    Range = min(m,n)
    result = 1
    for i in range(1,Range):
        if(m%i==0 & n%i==0):
            result = i

    return result


def gcd_recursion(m,n):
    Min_num = min(m,n)
    if (n==0):
        return m
    else:
        return gcd_recursion(n,m%n)


    




   

print(gcd_bruteForce(15,50))
print(gcd_recursion(15,50))

    



    



  