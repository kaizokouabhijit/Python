arr = [4,213,2323,43,432,16]
k = 3
n = len(arr)

def rotateinplace(arr):
    for i in range(k):
        temp = arr[n-1]
        # print(temp)
        for j in reversed(range(n)):
            print(j)
            if j ==0:
                arr[j] = temp
            else:
                arr[j] = arr[j-1]
       
    return arr





        
    


print(rotateinplace(arr))