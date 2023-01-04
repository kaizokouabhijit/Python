# Given a binary array, find max occurence of consecutive ones
arr = [1,1,0,1,1,1]


def maxoccurence(arr):
    max_count = 0
    count = 0
    for i in range(len(arr)):
        if arr[i] ==1:
            count+=1
            if count>max_count:
                max_count = count
        if arr[i] ==0:
            count = 0
    return max_count


print(maxoccurence(arr))