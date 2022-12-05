

arr = [1,2,3,4,5,3,4,2]

def reverseArray(arr):
    right,left = len(arr) - 1,0

    while right>left:
        temp = arr[right]
        arr[right] = arr[left]
        arr[left] = temp

        right-=1
        left+=1
    return arr

print(reverseArray(arr))