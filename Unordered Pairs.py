n, k = map(int, input().split())
a = list(map(int, input().split()))

f = [0] * k
for i in a:
    f[i % k] += 1

ans = (f[0] * (f[0]-1)) // 2
for i in range(1, k//2+1):
    if i != k - i:
        ans += f[i] * f[k-i]
if k % 2 == 0:
    ans += (f[k//2] * (f[k//2]-1)) // 2

print(ans)
