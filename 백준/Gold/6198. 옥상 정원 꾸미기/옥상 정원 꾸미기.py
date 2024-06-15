n = int(input());

stack = [];
answer = 0;
for i in range(n):
    now = int(input());
    while len(stack) and stack[len(stack) - 1] <= now: 
        stack.pop();

    # now의 옥상을 볼 수 있는 빌딩 개수
    answer += len(stack);
    stack.append(now);
    
print(answer);