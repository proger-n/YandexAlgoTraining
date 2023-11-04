N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

def merge(arr1, arr2):
    arr_res = []
    i, j = 0, 0
    while (i!=len(arr1)) & (j!=len(arr2)):
        if (arr1[i] < arr2[j]):
            # t = arr1.pop(0)
            arr_res.append(arr1[i])
            i += 1
        else:
            # t = arr2.pop(0)
            arr_res.append(arr2[j])
            j += 1
    
    if i!=len(arr1):
        arr_res.extend(arr1[i:])
    elif j!=len(arr2):
        arr_res.extend(arr2[j:])

    return arr_res

print(*merge(A, B))