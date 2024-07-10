e, s, m = map(int, input().split(" "));

def calcCongruent(a, b, x, y):
    a = 0 if a == x else a;
    b = 0 if b == y else b;
    if x < y:
        a, b, x, y = b, a, y, x;
        
    for i in range(a + (not a) * x, x * y + 1, x):
        if i % y == b:
            return i;

print(calcCongruent(calcCongruent(e, s, 15, 28), m, 15 * 28, 19));