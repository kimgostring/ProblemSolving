n, s = map(int, input().split());
seq = list(map(int, input().split()));

cnt = 0;
def cntSubseq(acc, i):
    global cnt;
    
    if i == n:
        return;
    if acc + seq[i] == s:
        cnt += 1;       
        
    cntSubseq(acc, i + 1);
    cntSubseq(acc + seq[i], i + 1);

cntSubseq(0, 0);
print(cnt);