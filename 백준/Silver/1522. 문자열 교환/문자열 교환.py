s = input()
a_len = s.count('a')
s += s[:a_len] # 처음과 끝이 연결될 수 있으므로 

min_b_cnt = s[:a_len].count('b')
now_b_cnt = min_b_cnt
for i in range(a_len, len(s)):
  now_b_cnt -= (ord(s[i - a_len]) - ord('a'))
  now_b_cnt += (ord(s[i]) - ord('a'))
  if now_b_cnt < min_b_cnt:
    min_b_cnt = now_b_cnt

print(min_b_cnt)