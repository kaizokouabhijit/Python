

arr = [2,3,4,3,1,6]
arr1 = [1,2,3,4,5,6]


def isSorted(arr):
    issorted = True
    for i in range(1,len(arr)):
        if(arr[i]>=arr[i-1] ):
            continue
        else:
            issorted = False

    return issorted

print(isSorted(arr))




