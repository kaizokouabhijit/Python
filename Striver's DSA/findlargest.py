
arr = [10,9,5,3,12,45]

def findlargest(arr):
    largest = 0

    for i in arr:
        if i > largest:
            largest = i
    
    return largest


print(findlargest(arr))


def find_second_largest(arr):
    largest, second_largest = 0,0
    for i in arr:
        if i > largest:
            second_largest = largest
            largest = i
    return second_largest
print(find_second_largest(arr))