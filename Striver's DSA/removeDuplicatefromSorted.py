# return length of deduplicated array
arr = [1,2,2,3,4,4,5,6,5]

def deduplicatedarray(arr):
    k=0
    for i in range(1, len(arr)):
        
        if arr[i]!=arr[i-1]:
            arr[k] = arr[i-1]
            k+=1
    arr[k]=arr[-1]
    return k+1


print(deduplicatedarray(arr))