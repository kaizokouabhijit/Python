

arr = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
ele = 30


def findelement(arr, ele):
    unzip_lst = zip(*arr)

    for i in unzip_lst:
        print(i[1])




findelement(arr,ele)