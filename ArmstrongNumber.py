#  Armstrong number - 153 = 1^3+5^3+3^3



from click import Argument


def IsArmstrongNumber(N):
    temp = N
    res = 0
    count = 0

    while(N!=0):
        n = N%10
        count +=1
        N = N//10
    N = temp
    while(N!=0):
        n = N%10
        res = res + n**count
        N = N//10

    return (temp ==res)
    

print(IsArmstrongNumber(152))     