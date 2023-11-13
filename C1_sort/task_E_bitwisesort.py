N = int(input())
S = [0] * N
for i in range(N):
    S[i] = input()
m = len(S[0])


def print_dict(d, phase):
    print(f"Phase {phase}")
    for k, v in d.items():
        if len(v) != 0:
            print(k, end=" ")
            print(*[item + (', ' if i < len(v)-1 else '') for i, item in enumerate(v)])
        else:
            print(k, "empty")
    print("**********")
    phase += 1
    return phase


print("Initial array:")
print(*[item + (', ' if i < len(S)-1 else '') for i, item in enumerate(S)])
print("**********")
buckets_key = [f"Bucket {n}:" for n in range(10)]
buckets_value = [[] for n in range(10)]

buckets = dict(zip(buckets_key, buckets_value))

for i in range(len(S)):
    e = str(S[i])
    buckets[f"Bucket {e[m-1]}:"].append(e)
m -= 1
phase = 1
phase = print_dict(buckets, phase)

while m:
    for k, v in buckets.items():
        shift = 0
        for i_v in range(len(v)):
            if v[i_v-shift][m-1] != str(i_v):
                t = v.pop(i_v-shift)
                buckets[f"Bucket {t[m-1]}:"].append(t)
                shift += 1
    phase = print_dict(buckets, phase)
    m -= 1

S = []
for k, v in buckets.items():
    for i in v:
        S.append(i)

print("Sorted array:")
print(*[item + (', ' if i < len(S)-1 else '') for i, item in enumerate(S)], end="\n")
