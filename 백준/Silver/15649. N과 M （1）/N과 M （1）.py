def permutation(n, m, selected):
    if len(selected) == m:
        print(*selected);
        return;
    
    for next in [x for x in range(1, n + 1) if x not in selected]:
        selected.append(next);
        permutation(n, m, selected);
        selected.pop();
        
    return selected;
    
n, m = map(int, input().split());
permutation(n, m, []);