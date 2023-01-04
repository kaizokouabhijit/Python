
arr =[6,4,1,2,5]


def sortedRotated(arr):

    total_rotations = 0

    for i in range(1,len(arr)-1):
        if arr[i]<arr[i-1]:
            total_rotations+=1

        if arr[len(arr)-1]<arr[0]:
            total_rotations+=1
        
        if(total_rotations <= 1):
            return True

    return False

print(sortedRotated(arr))

