n = int(input());
arr = list(map(int, input().split()));
arr.sort();

m = int(input());
numsToFind = list(map(int, input().split()));

for i in range(m) :
    # arr 안에 numToFind 안의 숫자가 존재하는지 확인
    numToFind = numsToFind[i];
    left = 0;
    right = n - 1;
    
    result = 0;
    
    while left <= right and result == 0 :
        ind = (left + right) // 2;
    
        if numToFind > arr[ind] :
            # right 탐색
            left = ind + 1;
        elif numToFind < arr[ind] :
            # left 탐색
            right = ind - 1;
        else : 
            # 찾음
            result = 1;
            break;
    
    print(result);