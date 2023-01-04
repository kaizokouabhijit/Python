
arr = [4,4,2,1,2]


def singleoccurence(arr):
    res = 0
    for i in arr:
        res = res^i
    return res



print(singleoccurence(arr))