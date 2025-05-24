
def exp(a, n, mod):
    result = 1
    a = a % mod
    while n > 0:
        if n % 2 == 1:
            result = (result * a) % mod
        a = (a * a) % mod
        n = n // 2
    return result

def sum(a, n, m):
    if a == 1:
        return n % m
    mod = m * (a - 1)
    a_n = exp(a, n, mod)
    S = (a * (a_n - 1)) // (a - 1)
    return S % m

T = int(input())
results = []
for _ in range(T):
    a, n, m = map(int, input().split())
    result = sum(a, n, m)
    results.append(result)

print("\n".join(map(str, results)))