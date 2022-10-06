







def reverse_number(N):
    rev = 0
    while(N!=0):
        n = N%10
        rev = rev*10+n
        N = N//10

    


    return rev


# print(reverse_number(N))