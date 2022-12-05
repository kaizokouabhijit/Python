
arr = [0,1,2,5,8,4,3]

def Selectionsort(arr):

    for i in range(len(arr)-1):
        index = i

        for j in range(i, len(arr)):
            if arr[j]<arr[index]:
                index = j
            
            temp = arr[i]
            arr[i] = arr[index]
            arr[index] = temp
            print(arr)

    


Selectionsort(arr)