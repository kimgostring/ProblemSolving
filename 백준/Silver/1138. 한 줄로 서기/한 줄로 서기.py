N = int(input())
infos = list(map(int, input().split(" ")))

h = 1 # 키가 가장 작은 사람부터 순서대로 자리 찾아감 
left_slots = [i for i in range(N)] # 왼쪽에 위치한 빈 공간 수 
line = [0] * N # 정답 줄서기 
for info in infos:
  # 왼쪽에 info명의 키 큰 사람이 있으므로
  # 현재 사람이 서야 할 위치는 >= info
  i = info

  # 빈 자리가 아니거나, 키 큰 사람 인원수가 다를 경우
  # 다른 자리 찾아야 함 
  while line[i] or left_slots[i] != info:
    i = i + 1

  # 자리 확정 
  line[i] = h 

  # 빈 공간 수 update
  for j in range(i + 1, N): 
    left_slots[j] -= 1
  h += 1

print(*line)