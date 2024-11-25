n = int(input())

# 1. 에라토스테네스의 체 -> n보다 작거나 같은 소수 구하기
isPrime = [True] * (n + 1)
for p in range(2, n + 1):
    if not isPrime[p]:
        continue
    
    m = 2
    while p * m <= n:
        isPrime[p * m] = False
        m += 1

primes = list(map(lambda x : x[0], filter(lambda x : x[1], enumerate(isPrime))))[2:]
LEN = len(primes)

# 2. 투포인터
ans = 0
if n >= 2:
    s, e = 0, 1
    now = primes[s]
    while True:
        if now < n:
            if e >= LEN:
                break
            now += primes[e]
            e += 1
        else:
            if now == n:
                ans += 1
            now -= primes[s]
            s += 1
        
print(ans)