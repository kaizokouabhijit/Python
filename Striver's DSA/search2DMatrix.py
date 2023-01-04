

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 60


def SearchMatrix(matrix, target):

    n = len(matrix[0]) - 1
    for rows in matrix:
        if(target>=rows[0] & target<=rows[n]):
            if target in rows:
                return True
        
    return False



print(SearchMatrix(matrix, target))