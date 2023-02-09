word = input()

while word != "0" :
    length = len(word)
    
    flag = True
    for i in range(length // 2) :
        if word[i] != word[length - 1 - i] :
            flag = False
            break
    
    if flag :
        # 팰린드롬
        print('yes')
    else :
        print('no')
        
        
    word = input()