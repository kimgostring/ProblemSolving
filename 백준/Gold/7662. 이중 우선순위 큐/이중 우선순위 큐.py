import heapq;
import sys;
input = sys.stdin.readline;
t = int(input());

for _ in range(t):
    maxH, minH, delMaxH, delMinH = [], [], [], [];
    n = int(input());
    for __ in range(n):
        command, v = input().split(" ");
        v = int(v);
        
        if command == "I":
            heapq.heappush(maxH, -v);
            heapq.heappush(minH, v);
        else: # D
            if len(maxH) == len(delMaxH):
                continue;
            
            if v == 1:
                while delMaxH and maxH[0] == delMaxH[0]:
                    heapq.heappop(maxH);
                    heapq.heappop(delMaxH);
                v = heapq.heappop(maxH);
                heapq.heappush(delMinH, -v);
            else: # -1
                while delMinH and minH[0] == delMinH[0]:
                    heapq.heappop(minH);
                    heapq.heappop(delMinH);
                v = heapq.heappop(minH);
                heapq.heappush(delMaxH, -v);
    if len(maxH) == len(delMaxH):
        print("EMPTY");
    else:
        while delMaxH and maxH[0] == delMaxH[0]:
            heapq.heappop(maxH);
            heapq.heappop(delMaxH);
        while delMinH and minH[0] == delMinH[0]:
            heapq.heappop(minH);
            heapq.heappop(delMinH);

        print(-maxH[0], minH[0]);