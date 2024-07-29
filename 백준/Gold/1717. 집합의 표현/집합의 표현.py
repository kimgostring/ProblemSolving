import sys;
input = sys.stdin.readline;

n, m = map(int, input().rstrip().split(" "));
s = [x for x in range(n + 1)]; 

def adjust(a):
    shouldUpdated = [];
    while s[a] != a:
        shouldUpdated.append(a);
        a = s[a];
    for u in shouldUpdated:
        s[u] = a;
    
    return a;
    
for _ in range(m):
    op, a, b = map(int, input().rstrip().split(" "));
    if not op: # 합집합 연산
        adjust(a);
        adjust(b);
        if a == b or s[a] == s[b]:
            continue;
        if s[a] < s[b]:
            s[s[b]] = s[a];
            adjust(s[b]);
        else:
            s[s[a]] = s[b];
            adjust(s[a]);
        
    else: # 같은 집합인지 check
        adjust(a);
        adjust(b);
        print("YES" if s[a] == s[b] else "NO");