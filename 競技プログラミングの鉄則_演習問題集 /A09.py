from sys import stdin

input = stdin.readline 

h, w, n = map(int, input().split())

prefix_matrix = [[0] * (w + 2) for _ in range(h + 2)]

for _ in range(n):
  a, b, c, d = map(int, input().split())

  prefix_matrix[a][b] += 1
  prefix_matrix[a][d + 1] -= 1
  prefix_matrix[c + 1][b] -= 1
  prefix_matrix[c + 1][d + 1] += 1

for x in range(1, h + 1):
  for y in range(1, w + 1):
    prefix_matrix[x][y] += prefix_matrix[x][y - 1]
    
for y in range(1, w + 1):
  for x in range(1, h + 1):
    prefix_matrix[x][y] += prefix_matrix[x - 1][y]
    
for x in range(1, h + 1):
  print(*prefix_matrix[x][1:w+1])