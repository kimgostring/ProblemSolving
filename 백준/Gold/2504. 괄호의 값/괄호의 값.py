OPEN = ["(", "["];
CLOSE = [")", "]"];

str = input();
stack = [];
answer = [];

wrong = False;
mul = False;
for char in str:
    if char in OPEN:
        val = OPEN.index(char) + 2;
        answer.append((val, len(stack)));
        mul = False;

        stack.append(char);
        
    elif char in CLOSE:
        if not stack or CLOSE.index(char) != OPEN.index(stack[-1]):
            wrong = True;
            break;
        
        stack.pop();
        val, depth = answer.pop();
        while answer and depth == answer[-1][1]:
            val += answer.pop()[0];
            
        if mul:
            if not answer:
                wrong = True;
                break;
            answer.append((answer.pop()[0] * val, len(stack)));
        else:
            answer.append((val, len(stack)));
            mul = True;
    
    else:
        wrong = True;
        break;

print(0 if wrong or stack else sum(list(zip(*answer))[0]));