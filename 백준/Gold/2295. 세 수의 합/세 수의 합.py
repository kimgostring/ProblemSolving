n = int(input());
nums = [0] * n;
for i in range(n):
    nums[i] = int(input());
nums.sort();

sumOfTwos = set();
for i in range(n):
    for j in range(i, n):
        sumOfTwos.add(nums[i] + nums[j]);

answer = 0;
found = False;
for i in range(n - 1, -1, -1):
    for j in range(i):
        if nums[i] - nums[j] in sumOfTwos:
            answer = nums[i];
            found = True;
            break;
    if found:
        break;

print(answer);