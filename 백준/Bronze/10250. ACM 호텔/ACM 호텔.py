t = int(input())

for _ in range(t) :
    h, w, n = map(int, input().split())
    
    resultH = n % h
    resultW = n // h + 1
    
    if resultH == 0 :
        resultH = h
        resultW -= 1
    
    if resultW < 10 :
        resultW = '0' + str(resultW)
        
    print(str(resultH) + str(resultW))