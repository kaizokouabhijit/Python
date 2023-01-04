arr1 = [1,2,2,3,4,5,6]

arr2 = [2,2,5,6,8,9]

def union(arr1, arr2):

    arr3 = []
    for i in arr1:
        if i not in arr3:
            arr3.append(i)

    for j in arr2:
        if j not in arr3:
            arr3.append(j)

    return arr3

def intersection(arr1, arr2):
    arr3=[]
    for i in arr1 :
        if i in arr2 and i not in arr3:
            arr3.append(i)

    return arr3
            


print(union(arr1,arr2))

print(intersection(arr1,arr2))
    