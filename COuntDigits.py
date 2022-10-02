# count number of digits in a number


N = 1

def count_digit(N):
    count = 0
    while(N//10!=0):
        N = N//10
        count+=1
    return count+1

print(count_digit(N))