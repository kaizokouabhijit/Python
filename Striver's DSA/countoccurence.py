

arr = [1,2,3,4,5,4,3,4,5,6,4,5,6]
dict = {}

def countoccurence(arr):
    for i in arr:
        if i in dict.keys():
            dict[i] += 1
        else:
            dict[i] =1
    return dict


print(max(countoccurence(arr).values()))