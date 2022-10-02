
def check_Palindrome(N):
    temp = N
    rev = 0
    while (N!=0):
        n = N%10
        rev = rev*10+n
        N = N//10
    return (temp == rev)

print(check_Palindrome(121))
