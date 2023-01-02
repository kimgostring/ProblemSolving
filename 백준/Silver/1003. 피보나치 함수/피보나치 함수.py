n = int(input());
result = [[0] * 2 for _ in range(41)];

result[0] = [1, 0];
result[1] = [0, 1];

max = 1;
for i in range(n) :
    num = int(input());
    
    if num > max :
        max = num;
        for j in range(2, num + 1) :
            # 차례차례 개수 더해가기
            result[j][0] = result[j - 1][0] + result[j - 2][0];
            result[j][1] = result[j - 1][1] + result[j - 2][1];
         
    print(result[num][0], result[num][1]);