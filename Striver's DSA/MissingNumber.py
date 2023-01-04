'''
Given an array nums containing n distinct numbers in the range [0, n], return 
the only number in the range that is missing from the array.
'''


arr = [0,1,3]

def find_missing(arr):
    for i in range(len(arr)+1):
        if i not in arr:
            return i



print(find_missing(arr))