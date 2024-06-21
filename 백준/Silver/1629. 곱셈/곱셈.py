import sys
sys.setrecursionlimit(10 ** 6);

def pow(a, b, c):
    if b == 1:
        return a % c;    
    half = pow(a, b // 2, c);
    return (half ** 2) * (1 if b % 2 == 0 else a) % c;

a, b, c = map(int, input().split());
print(pow(a, b, c));