N = int(input())
A = list(map(int, input().split()))


def merge(arr1, arr2):
    arr_res = []
    i, j = 0, 0
    while (i != len(arr1)) & (j != len(arr2)):
        if (arr1[i] < arr2[j]):
            arr_res.append(arr1[i])
            i += 1
        else:
            arr_res.append(arr2[j])
            j += 1

    if i != len(arr1):
        arr_res.extend(arr1[i:])
    elif j != len(arr2):
        arr_res.extend(arr2[j:])

    return arr_res


def mergesort(arr):
    l = len(arr)
    if l > 1:
        m = l//2
        arr1 = arr[:m]
        arr2 = arr[m:]
        arr1 = mergesort(arr1)
        arr2 = mergesort(arr2)
        arr = merge(arr1, arr2)
        return arr
    return arr


A = mergesort(A)
print(*A)
