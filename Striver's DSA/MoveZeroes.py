

# Move all zeroes in arr to the end of the array with O(1) space complexity

arr = [1,0,4,5,0,7,9]

def moveZero(arr):
    i,j= 0,0
    for i in range(len(arr)):
    
        if(arr[i]==0):
            i+=1
        else:
            arr[i],arr[j] = arr[j],arr[i]
            j+=1

    return arr

print(moveZero(arr))