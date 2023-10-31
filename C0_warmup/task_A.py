N, M = map(int, input().split())
A = list(map(int, input().split()))
boundaries = []
for i in range(M):
    boundaries.append(input())

def find_num(A, b):
    L, R = map(int, b.split())
    a = A[L:R+1]
    min_num = min(a)
    # print(min_num)
    for i in a:
        if i != min_num:
            return i
    return "NOT FOUND"

for b in boundaries:
    print(find_num(A, b))
# print(f"N = {N}, M= {M}")
# print("A=", A)
# print(*boundaries, sep="\n")

