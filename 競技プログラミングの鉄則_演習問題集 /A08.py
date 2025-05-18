from sys import stdin

input = stdin.readline

h, w = map(int, input().split())

metrix = [list(map(int, input().split())) for _ in range(h)]
  
sum_metrix = [[0] * w for _ in range(h)]
  
sum_metrix[0][0] = metrix[0][0]

for i in range(1, w):
  sum_metrix[0][i] = sum_metrix[0][i - 1] + metrix[0][i]
  
for i in range(1, h):
  sum_metrix[i][0] = sum_metrix[i - 1][0] + metrix[i][0]
  
for x in range(1, h):
  for y in range(1, w):
    sum_metrix[x][y] = metrix[x][y] + sum_metrix[x - 1][y] + sum_metrix[x][y - 1] - sum_metrix[x - 1][y - 1]
    
q = int(input())

for _ in range(q):
  x1, y1, x2, y2 = map(int, input().split())
  
  x1 -= 1
  y1 -= 1
  x2 -= 1
  y2 -= 1
  
  result = sum_metrix[x2][y2]
  
  if x1 != 0:
    result -= sum_metrix[x1 - 1][y2]
  
  if y1 != 0:
    result -= sum_metrix[x2][y1 - 1]
    
  if x1 != 0 and y1 != 0:
    result += sum_metrix[x1 - 1][y1 - 1]
    
  print(result)