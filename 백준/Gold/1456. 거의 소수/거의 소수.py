import math

a, b = map(int, input().split())
sqrtb = math.floor(math.sqrt(b))

ans = 0
primes = []
isPrime = [True] * (sqrtb + 1)
for p in range(2, sqrtb + 1):
    if not isPrime[p]:
        continue
    
    primes.append(p)
    i = 2
    while p * i <= sqrtb:
        isPrime[p * i] = False
        i += 1

for p in primes:
    i = p * p
    while i <= b:
        ans += int(i >= a)
        i *= p
    
print(ans)