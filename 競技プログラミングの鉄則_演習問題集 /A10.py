from sys import stdin

input = stdin.readline

n = int(input())
vector = list(map(int, input().split()))
d = int(input())

left_max = [0] * (n + 2)
right_max = [0] * (n + 2)

for i in range(1, n + 1):
  left_max[i] = max(left_max[i - 1], vector[i - 1])
  right_max[n - i + 1] = max(right_max[n - i + 2], vector[n - i])

for i in range(d):
  start, end = map(int, input().split())
  
  print(max(left_max[start - 1], right_max[end + 1]))
