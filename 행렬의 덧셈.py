def solution1(arr1, arr2):
    for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            arr1[i][j] += arr2[i][j]
    return arr1

def solution2(arr1, arr2):
    import numpy as np
    np_arr1 = np.array(arr1)
    np_arr2 = np.array(arr2)
    return (np_arr1 + np_arr2).tolist()

arr1 = [[1,2],[2,3]]
arr2 = [[3,4],[5,6]]
print(solution1(arr1,arr2))

arr1 = [[1,2],[2,3]]
arr2 = [[3,4],[5,6]]
print(solution2(arr1,arr2))
