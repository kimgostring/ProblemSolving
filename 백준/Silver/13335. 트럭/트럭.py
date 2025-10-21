from collections import deque

n, w, L = map(int, input().split(" "))
trucks = list(map(int, input().split(" ")))

time = 0
trucks_on_bridge = deque([0] * w)
trucks_weight = 0
for truck in trucks:
  # 맨 끝 트럭 밀어내기 
  trucks_weight -= trucks_on_bridge.popleft()  
  time += 1

  # 이번 truck이 여전히 다리 위에 올라오지 못하는 경우
  # 다리 위에 있는 다른 truck들을 계속 밀어내야 함 
  while trucks_weight + truck > L:
    trucks_weight -= trucks_on_bridge.popleft()  
    trucks_on_bridge.append(0)
    time += 1
    
  # 이번 트럭 올리기
  trucks_on_bridge.append(truck)
  trucks_weight += truck

# 마지막 트럭 끝까지 이동  
time += w

print(time)