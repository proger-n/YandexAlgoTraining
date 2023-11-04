A = list(input())
B = list(input())
l_a = len(A)
l_b = len(B)
if l_a == l_b:
    A.sort()
    B.sort()
    for i in  range(l_a):
        if A[i] != B[i]:
            print("NO")
            break
    else:
        print("YES")
else:
    print("NO")