arr = [1,2,3,4,6,7,3,5]
key = 6

def linearsearch(arr, key):

    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1



print(linearsearch(arr,key))