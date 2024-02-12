def solution(citations):
    citations.sort(reverse=True);
    
    h = 0;
    for citation in citations:
        if citation <= h: 
            break;
        h += 1;
    
    return h;