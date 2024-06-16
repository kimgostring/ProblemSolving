from collections import deque;

t = int(input())
for t in range(t):
    funcs = input();
    n = int(input());
    nums = deque(filter(None, input()[1:-1].split(",")));
    
    isReversed = False;  
    isError = False;  
    for f in funcs:
        if f == "R":
            isReversed = not isReversed; 
        elif f == "D":
            if len(nums) > 0:
                nums.pop() if isReversed else nums.popleft();
            else:
                isError = True;
                break;

    if isError:
        print("error");
    else:
        print("[" + ",".join(reversed(nums) if isReversed else nums) + "]");