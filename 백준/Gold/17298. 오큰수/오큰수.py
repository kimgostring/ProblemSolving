n = int(input());
nums = list(map(int, input().split()));
nums.reverse();

stack = [];
answer = [];
for num in nums:
    nge = -1;
    while len(stack) and stack[len(stack) - 1] <= num: 
        stack.pop();

    if len(stack) > 0:
        nge = stack[len(stack) - 1];
    
    answer.append(nge);
    stack.append(num);
    
answer.reverse();
print(*answer);