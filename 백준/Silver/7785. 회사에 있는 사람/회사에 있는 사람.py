import sys;
input = sys.stdin.readline;

n = int(input());
records = [input().rstrip().split(" ") for _ in range(n)];
answer = set();
for person, kind in records:
    if kind == "enter":
        answer.add(person);
    elif person in answer:
        answer.remove(person);
    
print(*sorted([*answer], reverse=True), sep="\n");