tc = int(input());
for _ in range(tc):
    front = [];
    back = [];

    commands = input();
    for c in commands:
        if c == "<":
            if front:
                back.append(front.pop());
        elif c == ">":
            if back:
                front.append(back.pop());
        elif c == "-":
            if front:
                front.pop();
        else: 
            front.append(c);
    print(*front, *reversed(back), sep="");