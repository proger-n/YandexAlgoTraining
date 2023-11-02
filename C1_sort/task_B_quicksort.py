N = int(input())
A = list(map(int, input().split()))
# x = int(input())


def partition(l, r, sup_elem):
    global A
    arr_less = []
    arr_other = []
    while l <= r:
        if A[l] < sup_elem:
            arr_less.append(A[l])
        else:
            arr_other.append(A[l])
        l += 1
    A = arr_less + arr_other
    return len(arr_less)


def qs(l, r):
    if l <= r:
        x = A[l]
        p = partition(l, r-1, x)
        qs(l, p)
        qs(p, r)


# p = partition(0, N-1, x)
qs(0, N-1)
print(A)
