import random
N = int(input())
A = list(map(int, input().split()))


def partition(l, r, sup_elem, arr):
    Equal = 0
    Bigger = 0
    Now = 0
    while Now <= r-l:
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

    return Equal, Bigger


# x = random.randint(0, N)
# p = partition(0, N-1, x, A)
# print(A)
# print("x=", x)
# print("less count = ", p)
# print("NOT less count = ", N-p)

def qs(arr, l, r):
    if l != r:
        x = random.randint(l, r)
        e, b = partition(l, r, x, arr)
        qs(arr, l, e)
        qs(arr, b, r)


qs(A, 0, N-1)

print(*A)
