n = int(input());
heights = list(map(int, input().split()));

stack = [];
answer = [];
for [i, h] in enumerate(heights):
    while len(stack) > 0:
        topI, topH = stack[len(stack) - 1]
        if h < topH:
            # 탑에서 신호 수신
            answer.append(topI + 1);
            break;
        
        # 해당 탑에서는 수신 불가
        stack.pop();

    # 모든 탑에서 수신 불가
    if len(stack) == 0:
        answer.append(0);

    # 해당 탑 스택에 추가    
    stack.append((i, h));
    
print(*answer);