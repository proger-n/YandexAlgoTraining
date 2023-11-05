import random
N = int(input())
A = list(map(int, input().split()))
x = random.randint(0, N)


def partition(l, r, sup_elem, arr):
    Equal = 0
    Bigger = 0
    Now = 0
    while Now < len(arr):
        if arr[Now] < sup_elem:
            tmp = arr[Now]
            arr[Now] = arr[Bigger]
            arr[Bigger] = arr[Equal]
            arr[Equal] = tmp
            Bigger += 1
            Equal += 1
        elif arr[Now] == sup_elem:
            tmp = arr[Now]
            arr[Now] = arr[Bigger]
            arr[Bigger] = tmp
            Bigger += 1
        Now += 1

    return len(arr[:Equal])


p = partition(0, N-1, x, A)
# print(A)
print("x=", x)
print("less count = ", p)
print("NOT less count = ", N-p)
print(*A)
