k = int(input());

stack = [];
for _ in range(k):
    n = int(input());
    if n == 0:
        if stack:
            stack.pop();
    else:
        stack.append(n);
    
print(sum(stack));