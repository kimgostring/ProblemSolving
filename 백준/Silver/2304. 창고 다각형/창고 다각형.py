import sys
input = sys.stdin.readline

def calc_sub_area(cols, max_h):
  area = 0
  prev_l = 0
  prev_h = 0
  l_of_max_h = 0
  
  for l, h in cols:
    if h <= prev_h:
      continue

    area += abs(l - prev_l) * prev_h
    prev_l, prev_h = l, h

    if h == max_h:
      l_of_max_h = l
      break
  
  return area, l_of_max_h

n = int(input())
max_h = 0
cols = []
for i in range(n):
  l, h = map(int, input().split(" "))
  max_h = max(h, max_h)
  cols.append((l, h))
cols.sort(key = lambda x: x[0])

left_sub_area, left_l = calc_sub_area(cols, max_h)
right_sub_area, right_l = calc_sub_area(reversed(cols), max_h)
middle_sub_area = (right_l - left_l + 1) * max_h
print(left_sub_area + right_sub_area + middle_sub_area)