from sys import stdin

input = stdin.readline

h, w = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(h)]
  
prefix_sum = [[0] * (w + 1) for _ in range(h + 1)]

for x in range(1, h + 1):
  for y in range(1, w + 1):
    prefix_sum[x][y] = matrix[x - 1][y - 1] + prefix_sum[x][y - 1] + prefix_sum[x - 1][y] - prefix_sum[x - 1][y - 1]

q = int(input())

for _ in range(q):
  x1, y1, x2, y2 = map(int, input().split())
  
  result = prefix_sum[x2][y2] - prefix_sum[x1 - 1][y2] - prefix_sum[x2][y1 - 1] + prefix_sum[x1 - 1][y1 - 1]
    
  print(result)