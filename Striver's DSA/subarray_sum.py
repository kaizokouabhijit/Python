'''
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.
'''


arr = [1,2,4,0,3,1,2,0,1]
k = 3

def subarray(arr, k):
    count = 0
    curSum = 0
    prefixSum = {0:1}
    for i in arr:
        curSum+=i
        diff = curSum - k
        count +=prefixSum.get(diff, 0)
        prefixSum[curSum] = 1+ prefixSum.get(curSum,0)

    return count



print(subarray(arr,k))
