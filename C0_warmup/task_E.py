N = int(input())
A = list(map(int, input().split()))

sum_1 = [0] * N
sum_2 = [0] * N
sum_1[0] = A[0]
sum_2[N-1] = A[N-1]
for i in range(1, N):
    sum_1[i] = A[i] + sum_1[i-1]
    sum_2[N-1-i] = A[N-1-i] + sum_2[N-i]

for i in range(N):
    print(A[i]*(i+1) - sum_1[i] + sum_2[i] - A[i]*(N-i), end=" ")
