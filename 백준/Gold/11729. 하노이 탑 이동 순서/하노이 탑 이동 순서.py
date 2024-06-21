def hanoi(n, start, end):
    if n == 1:
        return 1, f"{start} {end}";
    
    else:  
        cnt = 0;
        answer = "";
        tmp = 6 - start - end; 
        
        cnt1, answer1 = hanoi(n - 1, start, tmp);
        cnt += cnt1;
        answer += answer1;
        
        cnt += 1;
        answer += f"\n{start} {end}";
        
        cnt2, answer2 = hanoi(n - 1, tmp, end);
        cnt += cnt2;
        answer += "\n" + answer2;
        
        return cnt, answer;

k = int(input());
cnt, answer = hanoi(k, 1, 3);

print(cnt);
print(answer);